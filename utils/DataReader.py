import os
import yaml
import pathlib

class DataReader:
    def __init__(self, datadir):
        self.datadir = datadir

    def readyaml(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
            data = yaml.load(data, Loader=yaml.FullLoader)
            return data

    def listfiles(self, re_path="*/*.yaml"):
        files = [*pathlib.Path(self.datadir).glob(re_path)]
        return files