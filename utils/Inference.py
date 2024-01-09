import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence
import numpy as np

from .DataReader import DataReader
from .Tokenizer import Tokenizer

class Inference():
    
    def __init__(self, model, device=torch.device("cuda:0")):
        self.model = model
        self.device = device
        self.reader = DataReader(datadir="data/test")
        self.tk = Tokenizer()

        
    def predict_one(self, yaml_path, beam_size=20, predict_step=5):
        self.model.eval()
        with torch.no_grad():
            data = self.reader.readyaml(yaml_path)
            seq = data["stdchange"]
            seq, seqlen = self.tk.tokenize(seq)
            seq = torch.Tensor(seq).long().to(self.device)
            _, avgpred, _ = self.beam_search(seq, seqlen, beam_size=beam_size, predict_step=predict_step)
        return avgpred
        
    def beam_search(self, seq, seqlen, beam_size, predict_step):
        self.model.eval()
        self.model.to(self.device)
        with torch.no_grad():
            h_state, c_state = self.model.init_h0(torch.randn(1, self.model.vocab_size).to(self.device)), \
                               self.model.init_c0(torch.randn(1, self.model.vocab_size).to(self.device))
            h_state, c_state = h_state.unsqueeze(0).repeat(self.model.layer*self.model.bi_factor, 1, 1), \
                               c_state.unsqueeze(0).repeat(self.model.layer*self.model.bi_factor, 1, 1) 
            k = beam_size
            for i in range(seqlen):
                current = float(seq[i].clone().detach().cpu().numpy())
                in_id = seq[i].unsqueeze(0)
                _, h_state, c_state = self.model.decode(in_id, h_state, c_state)

            topk_prev_tokens = torch.Tensor([[seq[seqlen]]] * k).long().to(self.device)  # [k, 1]
            topk_sequences = topk_prev_tokens  # [k, 1]
            topk_logps = torch.zeros(k, 1).to(self.device)  # [k, 1]
            complete_sequences, complete_sequence_logps = [], []    
            h_state, c_state = h_state.repeat(1, beam_size, 1), c_state.repeat(1, beam_size, 1)
            step = 1
            while True:         
                logit, h_state, c_state = self.model.decode(topk_prev_tokens.squeeze(1), h_state, c_state)
                logp = torch.nn.functional.softmax(logit, dim=1) # [k, vocab_size]
                logp = topk_logps.expand_as(logp) + logp  # [k, vocab_size]
                if step == 1:
                    topk_logps, topk_tokens = logp[0].topk(k, 0, True, True)  # [k,]
                else:
                    topk_logps, topk_tokens = logp.view(-1).topk(k, 0, True, True)  # [k,]
                prev_tokens = torch.div(topk_tokens, self.model.vocab_size, rounding_mode='floor')
                next_tokens = topk_tokens % self.model.vocab_size
                topk_sequences = torch.cat((topk_sequences[prev_tokens], next_tokens.unsqueeze(1)), dim=1) # [k, step + 1]
                incomplete_indices = [indice for indice, next_token in enumerate(next_tokens)]
                complete_indices = list(set(range(len(next_tokens))) - set(incomplete_indices))
                if len(complete_indices) > 0:
                    complete_sequences.extend(topk_sequences[complete_indices].tolist())
                    complete_sequence_logps.extend(topk_logps[complete_indices])
                k -= len(complete_indices) 
                # Proceed with incomplete sequences
                if k == 0:
                    break
                topk_sequences = topk_sequences[incomplete_indices]
                h_state = h_state[:, prev_tokens[incomplete_indices], :]
                c_state = c_state[:, prev_tokens[incomplete_indices], :]
                topk_logps = topk_logps[incomplete_indices].unsqueeze(1)
                topk_prev_tokens = next_tokens[incomplete_indices].unsqueeze(1)
                if step >= predict_step:
                    if len(complete_indices) == 0:
                        complete_sequences.extend(topk_sequences.tolist())
                        complete_sequence_logps.extend(topk_logps[incomplete_indices])
                    break
                step += 1    
            i_s = torch.topk(torch.Tensor(complete_sequence_logps), beam_size, sorted=True).indices
            res = []
            for i in i_s:
                complete_sequences[i] = [*map(lambda x: x - 1, complete_sequences[i])]
                res.append(complete_sequences[i])     
            res = [*map(lambda x: x[1:], res)]
            avgpred = sum([*map(lambda x: sum(x) / len(x), res)]) / len(res)
            return res, avgpred, current

    def greedy_search(self, seq, seqlen, predict_step):
        res, avgpred, current = self.beam_search(seq, seqlen, 1, predict_step)
        return res, avgpred, current



    def postprocess(self, x):

        res = []
        for item in x:
            item = np.asarray(item).astype(np.float32) - 50
            item /= 5.
            item = np.cumsum(item)
            res.append(item.tolist())
        return res
