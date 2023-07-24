from regexp import *

def main():
    str = input()
    # (0 | 1)*1(0 | 1)(0 | 1)
    E = Concat(Star(Or(Literal("0"), Literal("1"))), Concat(Literal("1"), Concat(Or(Literal("0"), Literal("1")), Or(Literal("0"), Literal("1")))))
    print( E.matches(str) )

if __name__ == "__main__":
    main()
