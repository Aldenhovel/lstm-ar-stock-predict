import matplotlib.pyplot as plt
import torch


def plot_fig(history, inference, future_3=None, future_5=None, future_10=None, future_greedy=None, max_step=10):
    fig = plt.figure(figsize=[15, 5])
    xmax = len(history) + max_step
    if future_10:
        future_min, future_max = 1e9, -1e9
        for i in range(len(future_10)):
            pred_curve = history + future_10[i][:xmax]
            pred_curve = inference.postprocess([pred_curve])[0]
            plt.plot(pred_curve, label="pred", color="#1b7c3d")
            future_min, future_max = min(future_min, pred_curve[-1]), max(future_max, pred_curve[-1])
        vline10 = plt.vlines(len(history) - 1 + 10, 0, future_max, linestyles="dashed", colors="#1b7c3d")
        plt.vlines(len(history) - 1 + 10, 0, future_min, linestyles="dashed", colors="#1b7c3d")
    if future_5:
        future_min, future_max = 1e9, -1e9
        for i in range(len(future_5)):
            pred_curve = history + future_5[i][:xmax]
            pred_curve = inference.postprocess([pred_curve])[0]
            plt.plot(pred_curve, label="pred", color="#2b6a99")
            future_min, future_max = min(future_min, pred_curve[-1]), max(future_max, pred_curve[-1])
        vline5 = plt.vlines(len(history) - 1 + 5, 0, future_max, linestyles="dashed", colors="#2b6a99")
        plt.vlines(len(history) - 1 + 5, 0, future_min, linestyles="dashed", colors="#2b6a99")
    if future_3:
        future_min, future_max = 1e9, -1e9
        for i in range(len(future_3)):
            pred_curve = history + future_3[i][:xmax]
            pred_curve = inference.postprocess([pred_curve])[0]
            plt.plot(pred_curve, label="pred", color="#f16c23")
            future_min, future_max = min(future_min, pred_curve[-1]), max(future_max, pred_curve[-1])
        vline3 = plt.vlines(len(history) - 1 + 3, 0, future_max, linestyles="dashed", colors="#f16c23")
        plt.vlines(len(history) - 1 + 3, 0, future_min, linestyles="dashed", colors="#f16c23")

    if future_greedy:
        future_min, future_max = 1e9, -1e9
        for i in range(len(future_greedy)):
            pred_curve = history + future_greedy[i][:xmax]
            pred_curve = inference.postprocess([pred_curve])[0]
            plt.plot(pred_curve, label="pred", color="#f16c23")
            future_min, future_max = min(future_min, pred_curve[-1]), max(future_max, pred_curve[-1])
        vlinegd = plt.vlines(len(history) - 1 + len(future_greedy[i][:xmax]), 0, future_max, linestyles="dashed",
                             colors="#f16cca")
        plt.vlines(len(history) - 1 + len(future_greedy[i][:xmax]), 0, future_min, linestyles="dashed",
                   colors="#f16cca")

    history = inference.postprocess([history])[0]
    today = plt.vlines(len(history) - 1, 0, history[-1], colors="gray")
    handles, labels = [today], ['today']
    if future_3: handles.append(vline3), labels.append('+3days')
    if future_5: handles.append(vline5), labels.append('+5days')
    if future_10: handles.append(vline10), labels.append('+10days')
    if future_greedy: handles.append(vlinegd), labels.append(f'greedy search: +{len(future_greedy[i][:xmax])} days')
    plt.legend(handles=handles, labels=labels, loc='best')

    plt.plot(history, color="black")
    plt.xlim([0, xmax])
    plt.xlabel("Time Step")
    plt.ylabel("Change %")
    plt.title("Prediction")
    plt.grid()

    return fig


def bs(model, inference, device, ds, tk, yaml_path):
    model.eval()
    with torch.no_grad():
        data = ds.reader.readyaml(yaml_path)
        end_date = data["end"]
        code = data['code']
        seq_raw = data["stdchange"]
        seq, seqlen = tk.tokenize(seq_raw)
        seq = torch.Tensor(seq).long().to(device)

        pred, _, _ = inference.greedy_search(seq.to(device), seqlen, predict_step=30)
        seq = seq.cpu().numpy().tolist()

        fig = plot_fig(history=seq[1: 1 + seqlen], future_greedy=pred, max_step=30, inference=inference)
        fig.savefig(f'./static/img/bs_{code}_{end_date}.svg', format='svg')
    return f'img/bs_{code}_{end_date}.svg'


def gs(model, inference, device, ds, tk, yaml_path):
    model.eval()
    with torch.no_grad():
        data = ds.reader.readyaml(yaml_path)
        end_date = data["end"]
        code = data['code']
        seq_raw = data["stdchange"]
        seq, seqlen = tk.tokenize(seq_raw)
        seq = torch.Tensor(seq).long().to(device)

        preds_3, _, _ = inference.beam_search(seq.to(device), seqlen, beam_size=10, predict_step=3)
        preds_5, _, _ = inference.beam_search(seq.to(device), seqlen, beam_size=20, predict_step=5)
        preds_10, _, _ = inference.beam_search(seq.to(device), seqlen, beam_size=50, predict_step=10)
        seq = seq.cpu().numpy().tolist()

        fig = plot_fig(history=seq[1: 1 + seqlen], future_3=preds_3, future_5=preds_5, future_10=preds_10, max_step=10, inference=inference)
        fig.savefig(f'./static/img/gs_{code}_{end_date}.svg', format='svg')
    return f'img/gs_{code}_{end_date}.svg'
