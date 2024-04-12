
from .energy import *
class IsingHamiltonian:
    def __init__(self, J, mus):
        self.J = J
        self.bs = BitString(len(mus))
        self.bs.set_config(mus.tolist())
        
    def compute_average_values(self, T):
        
        energy.compute_average_values(self.bs, self.J,T )