# Exemplo de NFA que aceita todas as strings binárias exceto 01, 101 e 0100
edges = {
    (0,'0') : [1],
    (0,'1') : [5],
    (1,'0') : [8],
    (1,'1') : [2],
    (2,'0') : [3],
    (2,'1') : [8],
    (3,'0') : [4],
    (3,'1') : [8],
    (4,'0') : [8], 
    (4,'1') : [8], 
    (5,'0') : [6],
    (5,'1') : [8],
    (6,'0') : [8],
    (6,'1') : [7],
    (7,'0') : [8],
    (7,'1') : [8],
    (8,'0') : [8],
    (8,'1') : [8],
}
initial   =  0 # estado inicial
accepting = [0, 1, 3, 5, 6, 8] # conjunto de estado final

def nfa(string, current, edges, accepting): 
    if string == "":
        return  current in accepting
    else:
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if nfa(string[1:], next, edges, accepting):
                    return True
        return False
        

string = input()
print ( nfa(string, initial, edges, accepting) )
