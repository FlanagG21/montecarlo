Getting Started
===============
This page details how to use the montecarlo package.
Usage
-------
Once installed you can use this package. This example calculates the average energy, of a given ising model set up with temperature = 1::
.. code-block:: python
    import montecarlo

    conf = montecarlo.BitString(N)
    mus = np.zeros(len(G.nodes()))

    if len(G.nodes()) != len(mus):
        error("DimensionMismatch")

    if len(G.nodes()) != len(mus):
        error(" Dimension Mismatch")
    J = [[] for i in G.nodes()]
    for e in G.edges:
        J[e[0]].append((e[1], G.edges[e]['weight']))
        J[e[1]].append((e[0], G.edges[e]['weight']))
    ham = montecarlo.IsingHamiltonian(J,mus)
    E, M, HC, MS = ham.compute_average_values(1)


