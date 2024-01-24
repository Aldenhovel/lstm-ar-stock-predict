import torchinfo
from flask import Flask, render_template, request, jsonify, send_file
from predict import *
from grab import *

import time


app = Flask(__name__, template_folder='./templates/', static_folder='./static/', static_url_path='')

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/get_image')
def get_image():
    data = request.get_json()
    url = data.url
    return send_file(url, mimetype='image/svg')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    code, end_date = data['code'], data['endDate']
    end_date = [int(x) for x in end_date.split('-')]
    end_date = datetime.date(*end_date)
    yaml_path = get_sample_by_code(code, end_date)
    bs_svg = bs(model, inference, device, ds, tk, yaml_path)
    gs_svg = gs(model, inference, device, ds, tk, yaml_path)
    return jsonify({'gs_img': gs_svg, 'bs_img': bs_svg})


@app.route('/check_conn', methods=['GET'])
def check_conn():
    return jsonify({'status': '0',
                    'conn_time': str((time.time() - config['start_gui_time']) // 1) + ' s',
                    'config': config,
                    })


if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from utils.Tokenizer import MAX_LEN, Tokenizer
    from utils.StockDataset import StockDataset
    from utils.Inference import Inference

    import torch
    import matplotlib.pyplot as plt

    config = dict()
    config['model'] = 'LSTM'
    config['checkpoint_path'] = "../checkpoints/model-pretrained.pt"
    config['checkpoint'] = config['checkpoint_path'].split('/')[-1]
    config['device'] = 'cuda' if torch.cuda.is_available() else 'cpu'
    config['start_gui_time'] = time.time()

    device = torch.device(config['device'])
    model = torch.load(config['checkpoint_path'], map_location=device)
    model.device = device
    inference = Inference(model=model, device=device)

    tk = Tokenizer(grid=100, maxlen=MAX_LEN)
    ds = StockDataset("../data/test", r"*.yaml", tokenizer=tk)

    app.run()
