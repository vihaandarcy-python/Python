Number_of_tables = int(input("PLease neter how many tables you want: "))

for i in range(1, Number_of_tables+1):
    for j in range(1,11):
        print(i,"*",j," = ",i*j, sep="")