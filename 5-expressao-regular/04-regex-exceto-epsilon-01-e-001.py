from regexp import *

def main():
    str = input()
    # (0 | 1) | (00 | (1(0 | 1)) | (000 | 01(0 | 1) | 1(0 | 1)(0 | 1)) | ((0 | 1)(0 | 1)(0 | 1)(0 | 1)(0 | 1)*))

    # (0 | 1)
    # (00 | (1(0 | 1)))
    # (000 | 01(0 | 1) | 1(0 | 1)(0 | 1))
    # ((0 | 1)(0 | 1)(0 | 1)(0 | 1)(0 | 1)*)

    fst = Or(Literal("0"), Literal("1"))
    snd = Or(Literal("00"), Concat(Literal("1"), Or(Literal("0"), Literal("1"))))
    trd = Or(Literal("000"), Or(Concat(Literal("01"), Or(Literal("0"), Literal("1"))), Concat(Literal("1"), Concat(Or(Literal("0"), Literal("1")), Or(Literal("0"), Literal("1"))))))
    fth = Concat(Or(Literal("0"), Literal("1")), Concat(Or(Literal("0"), Literal("1")), Concat(Or(Literal("0"), Literal("1")), Concat(Or(Literal("0"), Literal("1")), Star(Or(Literal("0"), Literal("1")))))))

    E = Or(Or(fst, snd), Or(trd, fth))

    print( E.matches(str) )

if __name__ == "__main__":
    main()
