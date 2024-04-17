import pathlib
import os
from datetime import datetime
import time
import torch

import sys

sys.path.append('..')
from utils.Tokenizer import MAX_LEN, Tokenizer
from utils.StockDataset import StockDataset
from utils.Inference import Inference


def flattenList(x):
    res = []
    for item in x:
        if isinstance(item, list):
            res.extend(flattenList(item))
        else:
            res.append(item)
    return res


def getCheckpointsFilesName():
    files_name = os.listdir('../checkpoints/')
    files_name = [*filter(lambda x: x.endswith('.pt'), files_name)]
    return files_name


def unpackGreedySearchProfile(data):
    checkpoint = data['checkpoint']
    search_step = data['searchStep']
    code = data['code']
    date = '-'.join([str(data['dateY']), str(data['dateM']), str(data['dateD'])])
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    date = date_obj.strftime('%Y-%m-%d')
    return checkpoint, search_step, code, date

def unpackBeamSearchProfile(data):
    checkpoint = data['checkpoint']
    search_step = data['searchStep']
    code = data['code']
    date = '-'.join([str(data['dateY']), str(data['dateM']), str(data['dateD'])])
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    date = date_obj.strftime('%Y-%m-%d')
    beam_size = data['beamSize']
    return checkpoint, search_step, code, date, beam_size


class ModelState:

    def __init__(self):
        self.config = dict()
        self.config['checkpoint_dir'] = "../checkpoints/"
        self.config['checkpoint'] = 'model-pretrained.pt'
        self.config['device'] = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.config['start_gui_time'] = time.time()

        self.device = torch.device(self.config['device'])
        self.model = torch.load(self.config['checkpoint_dir'] + self.config['checkpoint'], map_location=self.device)
        self.model.device = self.device
        self.inference = Inference(model=self.model, device=self.device)

        self.tk = Tokenizer(grid=100, maxlen=MAX_LEN)
        self.ds = StockDataset("../data/test", r"*.yaml", tokenizer=self.tk)

    def updateState(self, state: dict):
        if 'checkpoint' in state and state['checkpoint'] != 'default' and state['checkpoint'] != self.config['checkpoint']:
            self.config['checkpoint'] = state['checkpoint']
            self.model = torch.load(self.config['checkpoint_dir'] + self.config['checkpoint'], map_location=self.device)
            self.model.device = self.device
            self.inference = Inference(model=self.model, device=self.device)


