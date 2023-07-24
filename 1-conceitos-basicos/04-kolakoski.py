def switch1and2(n):
    n = 2 if n == 1 else 1

def kolakoski():
    yield 1
    yield 2
    yield 2
    
    # utilize a sequência para descobrir o tamanho dos blocos seguintes
    gerador = kolakoski()
    next(gerador)
    next(gerador)
    n = next(gerador)
    
    i = 1
    
    while True:
        for a in range(n):
            yield i
        switch1and2(i)
        n = next(gerador)

def main():
    n = int(input())
    gerador = kolakoski()
    l = [ next(gerador) for i in range(n)]
    print(l)

if __name__ == "__main__":
    main()
