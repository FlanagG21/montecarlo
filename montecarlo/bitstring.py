
import numpy as np
class BitString:
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int)

    def __repr__(self):
        pass

    def __eq__(self, other):
        if other is None :
            return False
        if type(self) != type(other) :
            return False
        if self.N != other.N :
            return False              
        return np.array_equal(self.config, other.config)


    
    def __len__(self):
        return self.N

    def on(self):
        return self.config.sum()

    
    def off(self):
        return self.N - self.config.sum()
    
    def flip_site(self,i):
        self.config[i] = (self.config[i] + 1) % 2 
    
    def int(self):
        num = 0
        for i, bit in enumerate(reversed(self.config)):
            num += bit * (2 ** i)
        return num

    def set_config(self, s:list[int]):
        for i, bit in enumerate(s):
            self.config[i + (self.N - len(s))] = bit
        
    def set_int_config(self, dec:int):        
        for i in range(len(self.config)):
            self.config[i] = dec % 2
            dec //= 2
        self.config = self.config[::-1]
        



    def __str__(self):
        builder = ""
        for bit in self.config:
            builder += str(bit)
        return builder
