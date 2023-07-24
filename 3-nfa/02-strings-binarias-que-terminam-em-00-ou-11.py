# Exemplo de NFA que aceita as strings binárias que terminam em 00 ou 11
edges = {
    (1,'0') : [1, 2],
    (1,'1') : [1, 4],
    (2,'0') : [3],
    (4,'1') : [5], 
}
initial   =  1 # estado inicial
accepting = [3, 5] # conjunto de estado final

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
