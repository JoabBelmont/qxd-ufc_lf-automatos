def golumb():
    yield 1
    yield 2
    yield 2
     #use o gerador para descobrir quantas vezes o número n deve ser repetido de maneira recursiva
    gerador = golumb()
    next(gerador)
    next(gerador)
    n = 3
    
    for a in gerador:
        for i in range(a):
            yield n
        n += 1

def main():
    n = int(input())
    gerador = golumb()
    l = [next(gerador) for i in range(n)]
    print(l)


if __name__ == "__main__":
    main()
