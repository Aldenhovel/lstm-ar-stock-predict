MAX_LEN = 90

import random

class Tokenizer:
    def __init__(self, grid=100, maxlen=MAX_LEN):
        self.grid = grid
        self.tick = 10 / (self.grid / 2)
        self.maxlen = maxlen
        self.pad = 0
        self.vocab_size = self.grid + 1

    def show(self):
        print(f"grid: {self.grid}")
        print(f"tick: {self.tick}")

    def tokenize(self, seq):
        seq = [*map(lambda x: x // self.tick + self.grid / 2, seq)]
        seq = [*map(lambda x: x if x < self.grid else self.grid, seq)]
        seq = [*map(lambda x: x if x > 0 else 0, seq)]
        seqlen = len(seq)
        seq = [seq[0] + 1] + [*map(lambda x: int(x + 1), seq)] + [self.pad] * self.maxlen
        seq = seq[:self.maxlen]
        return seq, seqlen
    
    
class RandomCropTokenizer:
    def __init__(self, grid=100, maxlen=MAX_LEN, minlen=1):
        self.grid = grid
        self.tick = 10 / (self.grid / 2)
        self.maxlen = maxlen
        self.pad = 0
        self.vocab_size = self.grid + 1
        
        self.minlen = minlen
        

    def show(self):
        print(f"grid: {self.grid}")
        print(f"tick: {self.tick}")

    def tokenize(self, seq):
        seq = [*map(lambda x: x // self.tick + self.grid / 2, seq)]
        seq = [*map(lambda x: x if x < self.grid else self.grid, seq)]
        seq = [*map(lambda x: x if x > 0 else 0, seq)]
        seqlen = len(seq)
        
        if seqlen <= self.minlen:
            print(seqlen, self.minlen)
        newseqlen = random.randint(self.minlen, seqlen)
        startpoint = random.randint(0, seqlen - newseqlen)
        newseq = seq[startpoint: startpoint + newseqlen]
        
        seq, seqlen = newseq, newseqlen
        
        seq = [seq[0] + 1] + [*map(lambda x: int(x + 1), seq)] + [self.pad] * self.maxlen
        seq = seq[:self.maxlen]
        return seq, seqlen