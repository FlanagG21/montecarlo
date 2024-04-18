"""
Unit and regression test for the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import montecarlo as montecarlo



def test_montecarlo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo" in sys.modules

N = 6
Jval = 2.0
G = nx.Graph()
G.add_nodes_from([i for i in range(N)])
G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
for e in G.edges:
    G.edges[e]['weight'] = Jval


def test_montecarlo():
    # Define a new configuration instance for a 6-site lattice
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
    # Compute the average values for Temperature = 1
    E, M, HC, MS = ham.compute_average_values(1)


    print(" E  = %12.8f" %E)
    print(" M  = %12.8f" %M)
    print(" HC = %12.8f" %HC)
    print(" MS = %12.8f" %MS)

    assert(np.isclose(E,  -11.95991923))
    assert(np.isclose(M,   -0.00000000))
    assert(np.isclose(HC,   0.31925472))
    assert(np.isclose(MS,   0.01202961))
