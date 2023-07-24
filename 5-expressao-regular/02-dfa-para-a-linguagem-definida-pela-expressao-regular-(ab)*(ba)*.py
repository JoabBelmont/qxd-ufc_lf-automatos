# DFA para a linguagem definida pela expressão regular (ab)*(ba)*

# Coloque aqui as transições do seu autômato
edges = {
    (0,'a') : 1,
    (0,'b') : 4,
    (1,'a') : 3,
    (1,'b') : 2,
    (2,'a') : 1,
    (2,'b') : 4,
    (3,'a') : 3,
    (3,'b') : 3,
    (4,'a') : 5,
    (4,'b') : 3,
    (5,'a') : 3,
    (5,'b') : 4,
}

#Coloque aqui os estados finais do seu autômato
accepting = [0,2,5]

initial   = 0

# Função que roda o autômato
def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstate = edges[(current, letter)]
            return dfa(remainder, newstate, edges, accepting)
        return False


string = input()
print(dfa(string, initial, edges, accepting))