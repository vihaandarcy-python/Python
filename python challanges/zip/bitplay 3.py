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


def divide(ourDividend, ourDivisor):

    sign = (-1 if((ourDividend < 0) ^ (ourDivisor < 0)) else 1)

    ourDividend = abs(ourDividend)
    ourDivisor = abs(ourDivisor)

    quotientNumber = 0
    tempNumber = 0

    for i in range(31, -1, -1):

        if (tempNumber + (ourDivisor << i) <= ourDividend):
            tempNumber += ourDivisor << i
            quotientNumber |= 1 << i

    if sign == -1 :
        quotientNumber=-quotientNumber
    return quotientNumber


a = int(input("Enter a for a/b : "))
b = int(input("Enter b for a/b :"))
print("result of ",a,"/",b,"is",divide(a, b))
