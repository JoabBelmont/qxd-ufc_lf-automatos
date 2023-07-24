def is_ε(s):
    return s == None or s == ""

def prefixo(x, y):
    if is_ε(x):
        return True
    elif not is_ε(x) and is_ε(y):
        return False
    else:
        return x[0] == y[0] and prefixo(x[1:], y[1:])


def main():
    x = input()
    y = input()
    print( prefixo(x,y) )


if __name__ == "__main__":
    main()
