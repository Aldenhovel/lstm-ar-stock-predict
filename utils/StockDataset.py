import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from .Tokenizer import Tokenizer, MAX_LEN
from .DataReader import DataReader
import os
import tqdm
import datetime

class StockDataset(Dataset):
    def __init__(self, datadir, re_path, tokenizer):
        Dataset.__init__(self)
        self.datadir = datadir
        self.reader = DataReader(datadir)
        self.tk = tokenizer
        self.files = self.reader.listfiles(re_path)
        self.file_size = len(self.files)
        self.min_filter_seqlen = 31
        
    def __getitem__(self, index):
        file = self.reader.readyaml(self.files[index])
        stdfenshi = file["stdchange"]
        stdfenshi, seqlen = self.tk.tokenize(stdfenshi)
        stdfenshi = torch.Tensor(stdfenshi).long()
        return stdfenshi, seqlen
    
    def __len__(self):
        return self.file_size
    
    def checkds(self):
        print(f'Checking dataset in [{self.datadir}], include [{len(self.files)}] samples.')
        print(f'The min seqlen of data is [{self.min_filter_seqlen}], sample which under this standard would be removed.')
        remove_count = 0
        for ix in tqdm.tqdm(range(self.file_size)):
            file = self.reader.readyaml(self.files[ix])
            stdfenshi = file["stdchange"]
            stdfenshi, seqlen = self.tk.tokenize(stdfenshi)
            if seqlen < self.min_filter_seqlen:
                remove_count += 1
                file_path = str(self.files[ix]).replace('\\', '/')
                os.remove(file_path)
                print(f'Remove {file_path}.')
        print(f'Done. [{remove_count}] sample(s) removed.')
        