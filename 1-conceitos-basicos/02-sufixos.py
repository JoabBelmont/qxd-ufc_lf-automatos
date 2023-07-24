def sufixos(x):
    if x == None or x == "":
        return []
    else:
        return [x] + sufixos(x[1:])

def main():
    x = input()
    print( sufixos(x) )


if __name__ == "__main__":
    main()
