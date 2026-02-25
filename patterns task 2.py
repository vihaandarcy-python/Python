#Take input from user
rows = int(input("Please Enter the total number of Rows: "))
number = 1 #initialise by 1

print("Floyd's triangle")
#outer loop for number of rows
for i in range(1, rows +1):
    #inner loop for number of colums
    for j in range(1,i+1):
    #display resukt
        print(number, end=" ")
        number = number +1
    print()