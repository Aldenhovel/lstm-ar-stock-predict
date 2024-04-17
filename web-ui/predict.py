from backend import ModelState
import torch
from backend import flattenList


def greedySearch(model_state: ModelState, yaml_path: str, search_step: int):
    model_state.model.eval()
    with torch.no_grad():
        data = model_state.ds.reader.readyaml(yaml_path)
        seq_raw = data["stdchange"]
        trade_date = data['tradedate']
        open_ = data['open']
        close_ = data['close']
        high_ = data['high']
        low_ = data['low']

        seq, seqlen = model_state.tk.tokenize(seq_raw)
        seq = torch.Tensor(seq).long().to(model_state.device)

        preds, _, _ = model_state.inference.greedy_search(
            seq.to(model_state.device),
            seqlen,
            predict_step=search_step
        )
        pd = [(x - 50) * 0.002 + 1 for x in flattenList(preds)]
        pdp = [close_[-1]]
        for i in range(len(pd)):
            pdp.append(round(pdp[-1] * pd[i], 2))
        pd = pdp
        assert len(open_) == len(close_) == len(high_) == len(low_)
        gt = []
        for i in range(len(open_)): gt.append([open_[i], close_[i], high_[i], low_[i]])
        trade_date.extend([f'+{i}' for i in range(1, len(pd))])
        return {
            'gt': gt,
            'pd': pd,
            'xaxis': trade_date,
        }


def beamSearch(model_state: ModelState, yaml_path: str, search_step: int, beam_size: int):
    model_state.model.eval()
    with torch.no_grad():
        data = model_state.ds.reader.readyaml(yaml_path)
        seq_raw = data["stdchange"]
        trade_date = data['tradedate']
        open_ = data['open']
        close_ = data['close']
        high_ = data['high']
        low_ = data['low']

        seq, seqlen = model_state.tk.tokenize(seq_raw)
        seq = torch.Tensor(seq).long().to(model_state.device)

        preds, _, _ = model_state.inference.beam_search(
            seq.to(model_state.device),
            seqlen,
            beam_size=beam_size,
            predict_step=search_step
        )

        pdp = []
        for i in range(beam_size):
            pdp_i = [close_[-1]]
            for j in range(len(preds[0])):
                pdp_i.append(round(pdp_i[-1] * ((preds[i][j] - 50) * 0.002 + 1), 2))
            pdp.append(pdp_i)
        pd = pdp
        assert len(open_) == len(close_) == len(high_) == len(low_)
        gt = []
        for i in range(len(open_)): gt.append([open_[i], close_[i], high_[i], low_[i]])
        trade_date.extend([f'+{i}' for i in range(1, len(pd[0]))])
        return {
            'pd': pd,
            'xaxis': trade_date,
            'gt': gt,
        }
