from .bitstring import *
import numpy as np
def energy(bs: BitString, J: list[list]):
    energy = 0.0
    for u in range(len(J)):
        for v in range(len(J[u])):
            if bs.config[u] == bs.config[v]:
                energy += J[u][v]
            else:
                energy -= J[u][v]
    return energy

k =  1
def compute_average_values(bs:BitString, J: list[list], T: float):
    E = 0
    M = 0
    HC = 0
    MS = 0

    z = boltzmanDenominator(bs, J, T)
    for i in range(2 ** bs.N):
        bs.set_int_config(i)
        currEnergy = energy(bs, J)
        p = np.e ** ((-1 / (k * T))* currEnergy)
        p /= z
        E += currEnergy*p
        currEnergySquared = currEnergy ** 2
        HC += currEnergySquared * p
        mag = bs.on() - bs.off()
        M += mag * p
        magSQR = mag**2
        MS += magSQR * p
    MS = (MS - M**2) * T ** -1        
    HC = (HC - E**2) * T ** -2
    
    return E, M, HC, MS

def boltzmanDenominator(bs:BitString, J: list[list], T: float):
    z = 0
    z2 = 0
    zm = 0
    zm2 = 0
    for i in range(2 ** bs.N):
        bs.set_int_config(i)
        currEnergy = energy(bs, J)
        z += np.e ** ((-1 / (k * T))* currEnergy)
    return z