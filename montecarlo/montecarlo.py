
from .energy import *
class IsingHamiltonian:
    """
    Class representing the Ising Hamiltonian system.

    :param J: List of lists representing interactions between spins.
    :param mus: Array representing the initial configuration of spins.
    """
    def __init__(self, J, mus):
        """
        Initialize the IsingHamiltonian object.

        :param J: List of lists representing interactions between spins.
        :param mus: Array representing the initial configuration of spins.
        """
        self.J = J
        self.bs = BitString(len(mus))
        self.bs.set_config(mus.tolist())
        
    def compute_average_values(self, T):
        """
        Compute average values of energy, magnetization, heat capacity, and magnetic susceptibility.

        :param T: Temperature.
        :return: Tuple of energy, magnetization, heat capacity, and magnetic susceptibility.
        """
        return compute_energy_average_values(self.bs, self.J, T)