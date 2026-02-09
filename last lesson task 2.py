print("enter a number (numerator): ")
numn = int(input())
print("Enter a Number (denominator): ")
numd =int(input())

if numn%numd==0:
    print("\n" + str(numn) + " is divisible by", numd)
else:
    print("\n" + str(numn) + " is not divisible by", numd)