def main():
    # ['0','1']
    # ([1, 2, 3], {(1, '1'): 1, (1, '0'): 2, (2, '0'): 2, (2, '1'): 3, (3, '0'): 3, (3, '1'): 3}, 1, [3])
    # ([1, 2], {(1, '1'): 1, (1, '0'): 2, (2, '0'): 1, (2, '1'): 2}, 1, [1])

    sigma = eval(input())
    (states1, edges1, initial1, final1) = eval(input())
    (states2, edges2, initial2, final2) = eval(input())
    
    #adicionando um par ordenado relacionando
    #os dois autômatos 

    # states3 -> [(x,y)]
    states3 = []
    for x in states1:
        for y in states2:
            states3.append( (x,y) )
    
    # edges3 -> {((x,y),w): (x',y')}
    edges3 = {}
    for e in states3:
        for w in sigma:
            edges3[ ((e[0], e[1]), w) ] = (edges1[(e[0], w)], edges2[(e[1], w)])
    
    # final3 -> [(x,y)]
    final3 = []
    for x in states3:
        for f1 in final1:
            for f2 in final2:
                if x[0] == f1 or x[1] == f2:
                    final3.append(x)
                
    
    initial3 = (initial1, initial2)
    
    teste(states3, edges3, initial3, final3)
