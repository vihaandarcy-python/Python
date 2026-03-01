def hello(n):
    if n > 1:
        hello(n//2)
    print(n % 2,end='')

#decimal number
    dec = 13
    
    hello(dec)
    print()