import torch
import torch.nn as nn

class MyLoss(nn.Module):
    
    def __init__(self, device):
        nn.Module.__init__(self)
        self.kernel = torch.Tensor([[[[0.1, 0.2, 0.4, 0.2, 0.1]]]]).to(device)
        self.alpha = 10
        self.kl_div = nn.KLDivLoss(log_target=True)
        self.device = device
        
    def forward(self, pred, gt):
        assert len(pred.shape) == 2
        assert len(gt.shape) == 1
        
        pred = nn.functional.softmax(pred, dim=-1)
        gt = nn.functional.one_hot(gt, num_classes=pred.shape[-1]).float().unsqueeze(0).unsqueeze(0)
        gt = nn.functional.conv2d(gt, weight=self.kernel, padding=(0, 2))
        gt = nn.functional.softmax(gt*self.alpha, dim=-1)
        loss = self.kl_div(pred, gt) * 1000
        return loss