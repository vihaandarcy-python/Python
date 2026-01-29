#take marks as input from user
print("Enter Marks obtaines in 4 subjects: \n")

math = int(input("math :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

#Lets calculate the percentage of marks
sum = math+english+science+hindi
print("sum of math, english, science and hindi is", sum, "\n")

perc = (sum/400)*100

print(end =" Total Percentage Mark = ")
print(perc)

