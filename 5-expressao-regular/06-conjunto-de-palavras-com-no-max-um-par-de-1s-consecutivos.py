from regexp import *

def main():
    str = input()
    # 0* | (10|0)*1(10|0)* | (01|0)*1(01|0)* | 11(01)*
    fst = Star(Literal("0"))
    snd = Star(Or(Literal("10"), Literal("0")))
    trd = Star(Or(Literal("01"), Literal("0")))
    fth = Concat(Literal("11"), Star(Literal("01")))

    E = Or(fst, Or(Concat(Concat(snd, Literal("1")), snd), Or(Concat(Concat(trd, Literal("1")), trd), fth)))

    print( E.matches(str) )

if __name__ == "__main__":
    main()
