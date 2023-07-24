# Strings binárias que tenha 1 nas últimas 4 posições
edges = {
    (0, '')  : [1,5],
    (1, '0') : [2],
    (1, '1') : [1],
    (2, '0') : [3],
    (2, '1') : [1],
    (3, '0') : [4],
    (3, '1') : [1],
    (4, '0') : [5],
    (4, '1') : [1],
    (5, '0') : [5],
    (5, '1') : [1]
}
initial   = 0
accepting = [1,2,3,4] 

def epsilon_nfa(string, current, edges, accepting):
    #print ("current: " + str(current) + "string: " + string )    
    if string == "":
        return  current in accepting
    else:
        if (current, '') in edges:
          for next in edges[(current,'')]:
            if epsilon_nfa(string, next, edges, accepting):
                    return True
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if epsilon_nfa(string[1:], next, edges, accepting):
                    return True

        return False

string = input()
print (epsilon_nfa( string , initial, edges, accepting) )