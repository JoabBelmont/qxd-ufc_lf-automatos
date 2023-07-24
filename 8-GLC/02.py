# Linguagem formada por {a,b,c} com pelo menos um a e pelo menos um b

from glc import GLC

def main():
    # S -> aT | bV | cS 
    # T -> aT | bU | cT
    # U -> aU | bU | aU | E
    # V -> aU | bV | cV 
    V = {'S', 'T', 'U', 'V'}
    Sigma = {'a', 'b', 'c'}
    R = {('S', 'aT'), ('S', 'bV'), ('S', 'cS'),
         ('T', 'aT'), ('T', 'bU'), ('T', 'cT'),
         ('U', 'aU'), ('U', 'bU'), ('U', 'cU'), ('U', ''),
         ('V', 'aU'), ('V', 'bV'), ('V', 'cV')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
