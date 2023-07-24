from regexp import *

def main():
    str = input()
    # (aa | bb)* | a(aa)*b(bb)*
    fst = Star(Or(Literal("aa"), Literal("bb")))
    snd = Concat(Literal('a'), Concat(Star(Literal("aa")), Concat(Literal('b'), Star(Literal("bb")))))
    E = Or(fst, snd)

    print( E.matches(str) )

if __name__ == "__main__":
    main()
