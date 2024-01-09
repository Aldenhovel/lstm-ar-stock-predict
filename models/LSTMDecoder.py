import torch
import torch.nn as nn

class LSTMDecoder(nn.Module):
    def __init__(self, vocab_size, hidden_dim=512, layer=2, bi=True, device=torch.device("cpu")):
        nn.Module.__init__(self)
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim
        self.layer = layer
        self.bi = bi
        self.bi_factor = 2 if self.bi else 1
        self.device = device
        self.embed = nn.Embedding(vocab_size, hidden_dim)
        self.init_h0 = nn.Linear(in_features=vocab_size, out_features=hidden_dim)
        self.init_c0 = nn.Linear(in_features=vocab_size, out_features=hidden_dim)
        self.lstm = nn.LSTM(input_size=hidden_dim, hidden_size=hidden_dim, num_layers=layer, bidirectional=bi)
        self.fc = nn.Linear(in_features=hidden_dim*self.bi_factor, out_features=vocab_size)
        self.dropout = nn.Dropout(p=0.3)
        
    def decode(self, tokens, h_state, c_state):
        x = self.embed(tokens)
        x, (h_state, c_state) = self.lstm(x.unsqueeze(0), (h_state, c_state))
        x = self.dropout(x)
        logit = self.fc(x).squeeze(0)
        return logit, h_state, c_state
    
    def forward(self, seqs, seqlens):
        batch_size = seqs.size()[0]
        sorted_seq_len, sorted_seq_indices = torch.sort(seqlens, dim=0, descending=True)
        sorted_seqs = seqs[sorted_seq_indices]
        h_state, c_state = self.init_h0(torch.randn(batch_size, self.vocab_size).to(self.device)),\
                           self.init_c0(torch.randn(batch_size, self.vocab_size).to(self.device))
        h_state, c_state = h_state.unsqueeze(0).repeat(self.layer*self.bi_factor, 1, 1),\
                           c_state.unsqueeze(0).repeat(self.layer*self.bi_factor, 1, 1) 
        sorted_decode_len = sorted_seq_len.tolist()  
        logits = torch.zeros(max(sorted_decode_len), batch_size, self.vocab_size)
        for t in range(max(sorted_decode_len)):
            batch_size_t = sum([l > t for l in sorted_decode_len])          
            batch_tokens = sorted_seqs[:batch_size_t, t]        
            logit, h_state, c_state = self.decode(batch_tokens, 
                                                  h_state[:, :batch_size_t, :].contiguous(), 
                                                  c_state[:, :batch_size_t, :].contiguous(), 
                                                  )
            logits[t, :batch_size_t, :] = logit.unsqueeze(0)       
        return logits, sorted_seqs, sorted_decode_len, sorted_seq_indices
    
        