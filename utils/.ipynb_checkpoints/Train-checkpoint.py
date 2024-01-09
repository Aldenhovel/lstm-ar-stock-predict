from tqdm import tqdm
import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence

def clip_gradient(optimizer, grad_clip):
    for group in optimizer.param_groups:
        for param in group['params']:
            if param.grad is not None:
                param.grad.data.clamp_(-grad_clip, grad_clip)
                
def train_step(model, optimizer, criterion, loader, epoch, device):
    losslst = []
    model.to(device)
    model.train()
    pbar = tqdm(enumerate(loader), total=len(loader), ncols=100)
    for i, (seqs, seqlens) in pbar:
        seqs = seqs.to(device)
        seqlens = seqlens.to(device)
        logits, sorted_seqs, sorted_decode_len, sorted_seq_indices = model(seqs, seqlens)
        logits = pack_padded_sequence(logits, sorted_decode_len).data
        gt = sorted_seqs[:, 1:]
        gt = pack_padded_sequence(gt, sorted_decode_len, batch_first=True).data   
        if type(criterion) == type(torch.nn.KLDivLoss()):

            preds = nn.functional.softmax(logits, dim=-1)
            gt = nn.functional.one_hot(gt.long(), num_classes=102)
            preds, gt = preds.float() + 1e-9, gt.float()
            loss = criterion(preds.to(device).log(), gt)
        elif type(criterion) == type(torch.nn.CrossEntropyLoss()):
            loss = criterion(logits.to(device), gt)
        else:
            assert(False)
        optimizer.zero_grad()
        loss.backward()
        clip_gradient(optimizer, 1e-3)
        optimizer.step()
        losslst.append(loss)
        pbar.set_description(f"Epoch: {epoch}, loss: {(sum(losslst) / len(losslst)):.5f}")
    return loss

def vaild_step(model, loader, epoch, device):
    corr, tot = 0, 0
    model.to(device)
    model.eval()
    pbar = tqdm(enumerate(loader), total=len(loader), ncols=100)
    for i, (seqs, seqlens) in pbar:
        seqs = seqs.to(device)
        seqlens = seqlens.to(device)
        logits, sorted_seqs, sorted_decode_len, sorted_seq_indices = model(seqs, seqlens)
        logits_copy = logits.clone()
        _, preds = torch.max(logits_copy, dim=2)
        preds = preds.t()
        preds = pack_padded_sequence(preds, sorted_decode_len, batch_first=True).data
        gt = sorted_seqs[:, 1:].detach().cpu()
        gt = pack_padded_sequence(gt, sorted_decode_len, batch_first=True).data
        for i in (gt - preds):
            if i == 0:
                corr += 1
            tot += 1
        pbar.set_description(f"Epoch: {epoch}, _acc: {(corr / tot):.5f} ({corr}/{tot})")
    return corr / tot

