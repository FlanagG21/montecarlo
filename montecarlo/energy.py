from .bitstring import *
import numpy as np
from typing import List 


def energy(bs: BitString, J: List[List]):
    """
    Calculate the energy of a given configuration.

    :param bs: BitString object representing the configuration.
    :param J: List of lists representing interactions between spins.
    :return: Energy of the configuration.
    """
    energy = 0.0
    for u, neighbors in enumerate(J):
        for v, weight in neighbors:
            if bs.config[u] == bs.config[v]:
                energy += weight
            else :
                energy -= weight
    return energy / 2

k =  1
def compute_energy_average_values(bs:BitString, J: List[List], T: float):
    """
    Compute energy, magnetization, heat capacity, and magnetic susceptibility.

    :param bs: BitString object representing the configuration.
    :param J: List of lists representing interactions between spins.
    :param T: Temperature.
    :return: Tuple of energy, magnetization, heat capacity, and magnetic susceptibility.
    """
    E = 0
    M = 0
    HC = 0
    MS = 0

    z = boltzmanDenominator(bs, J, T)
    """_summary_
    Compute energy, magnetization, heat capacity, and magnetic susceptibility.
    Returns:
        _type_: a touple of average energy, magnetization, Heat capacity and magnetic susceptibility.
    """
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

def boltzmanDenominator(bs:BitString, J: List[List], T: float):
    """_summary_
    private method do not call directly.
    """
    z = 0
    z2 = 0
    zm = 0
    zm2 = 0
    for i in range(2 ** bs.N):
        bs.set_int_config(i)
        currEnergy = energy(bs, J)
        z += np.e ** ((-1 / (k * T))* currEnergy)
    return z