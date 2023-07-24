# Linguagens formadas por 0's e 1's com no máximo um par de 1's consecutivos

from glc import GLC

def main():
    # S -> 0S | 1T | E
    # T -> 0S | 1T | E
    # U -> 0V | E
    # V -> 0V | 1U | E
    V = {'S', 'T', 'U', 'V'}
    Sigma = {'1', '0'}
    R = {('S', '0S'), ('S', '1T'), ('S', ''),
         ('T', '0S'), ('T', '1U'), ('T', ''),
         ('U', '0V'), ('U', ''),
         ('V', '0V'), ('V', '1U'), ('V', '')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
