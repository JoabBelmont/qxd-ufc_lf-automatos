# from glc import GLC

def main():
    # S -> aSb | bSa | E
    V = {'S'}
    Sigma = {'a', 'b'}
    R = {('S', 'aSb'), ('S', 'bSa'), ('S', 'abS'), ('S', 'baS'), ('S', '')}
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
    