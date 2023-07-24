# ([1, 2, 3], {(1, '1'): 1, (1, '0'): 2, (2, '0'): 2, (2, '1'): 3, (3, '0'): 3, (3, '1'): 3}, 1, [3])

def main():
      
    (states, edges, initial, final) = eval(input())
    
    states2 = states
    edges2 = edges
    initial2 = 0

    final2 = [x for x in states if x not in final]

    teste(states2, edges2, initial2, final2) 