def swap(a, b, c):
    a = a + b + c
    b = a - (b + c)
    c = a - (b + c)
    a = a - (b + c)

    print("after swapping a =", a, " b =", b, "c =", c)

swap (2, 7, 5)

def XOR(a, b, c):

    a = a^b^c
    b = a^b^c
    c = a^b^c
    a = a^b^c

    print("After using XOR methos: a =", a, "b =", b, "c =", c)

XOR(13, 35, 70)