#Input a number
num = int(input("Enter the number: "))
t = num
numlen = 0
#iterate the loop
while t >0:
    numlen = numlen +1
    t = int(t/10)

if numlen>=4: #condition 1
    numLen = int(numlen/2)
    chk = 0
    while num>0: #iterate loop
        rem = num%10
        if chk == numLen:
            midone = rem
        elif chk ==(numLen-1):
            midtwo = rem
        num = int(num/10)
        chk = chk+1
    prod = midone*midtwo #product of the middle digits
    #display the result
    print("\nProduct of Mid digits (" +str(midone)+ "*" +str(midtwo)+") =", prod)

else:
    print("\nIt's not a 4 or more 4-digit bumber!")
    