# Linguagem {a^ib^jc ^k | i >= 0, j>= 0, k = i+j}

from glc import GLC

def main():
    # S -> aSc | bTc | E
    # T -> bTc | E
    V = {'S', 'T'}
    Sigma = {'a', 'b', 'c'}
    R = {('S', 'aSc'), ('S', 'bTc'), ('S', ''),
         ('T', 'bTc'), ('T', '')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
