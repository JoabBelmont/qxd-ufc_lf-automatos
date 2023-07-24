# Linguagem formada por 0's e 1's que possui dois zeros consecutivos

from glc import GLC

def main():
    # S -> 1S | 0T
    # T -> 0U | 1S
    # U -> 1U | 0U | E
    V = {'S', 'T', 'U'}
    Sigma = {'1', '0'}
    R = {('S', '0T'), ('S', '1S'),
         ('T', '0U'), ('T', '1S'),
         ('U', '0U'), ('U', '1U'), ('U', '')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
