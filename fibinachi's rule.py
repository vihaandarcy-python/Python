amount_of_numbers = int(input("Enter the amount of numbers you want: "))

lastNum = 1
prevToLastNum = 0

for i in range(amount_of_numbers):
    newNumber = lastNum + prevToLastNum
    
    print(newNumber)

    prevToLastNum = lastNum
    lastNum = newNumber
    