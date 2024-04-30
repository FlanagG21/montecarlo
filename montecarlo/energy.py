
def compute_energy_average_values(self, T):
    """Compute Average values exactly

    Parameters
    ----------
    T      : int
        Temperature

    Returns
    -------
    E  : float
        Energy
    M  : float
        Magnetization
    HC : float
        Heat Capacity
    MS : float
        Magnetic Susceptability
    """
    E = 0.0
    M = 0.0
    Z = 0.0
    EE = 0.0
    MM = 0.0

    conf = montecarlo.BitString(self.N)

    for i in range(conf.n_dim):
        conf.set_int_config(i)
        Ei = self.energy(conf)
        Zi = np.exp(-Ei / T)
        E += Ei * Zi
        EE += Ei * Ei * Zi
        Mi = np.sum(2 * conf.config - 1)
        M += Mi * Zi
        MM += Mi * Mi * Zi
        Z += Zi

    E = E / Z
    M = M / Z
    EE = EE / Z
    MM = MM / Z

    HC = (EE - E * E) / (T * T)
    MS = (MM - M * M) / T
    return E, M, HC, MS