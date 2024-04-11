from .bitstring import *
import networkx as nx
def energy(bs: BitString, G: nx.Graph):
    energy = 0.0
    for u,v in G.edges():
        if bs.config[u] == bs.config[v]:
            energy += G.edges[u,v]["weight"]
        else:
            energy -= G.edges[u,v]["weight"]
    return energy

k =  1
def compute_average_values(bs:BitString, G: nx.Graph, T: float):
    E = 0
    M = 0
    HC = 0
    MS = 0

    z, z2, zm, zm2 = boltzmanDenominator(bs, G, T)
    for i in range(2 ** bs.N):
        bs.set_int_config(i)
        currEnergy = energy(bs, G)
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

def boltzmanDenominator(bs:BitString, G: nx.Graph, T: float):
    z = 0
    z2 = 0
    zm = 0
    zm2 = 0
    for i in range(2 ** bs.N):
        bs.set_int_config(i)
        currEnergy = energy(bs, G)
        z += np.e ** ((-1 / (k * T))* currEnergy)
        currEnergySquared = currEnergy ** 2
        z2 += np.e ** ((-1 / (k * T)) * currEnergySquared)
        mag = bs.on() - bs.off()
        magSQR = mag ** 2
        zm += np.e ** ((-1 / (k * T)) * mag)
        zm2 += np.e ** ((-1 / (k * T)) * magSQR)
    currEnergy = energy(bs, G)
    z += np.e ** ((-1 / (k * T)) * currEnergy)
    print((-1 / (k * T)))
    return z, z2, zm, zm2