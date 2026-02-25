#Take input
print("half pyramid pattern of stars (*): ")
n=int(input("Enter the number of rows"))
#outer loops to handle number of rows
for i in range(n):
    #inner loop to handle number of colums
        for j in range(i+1):
            print("* ", end="")
        print()