number = int(input("Enter your number: "))


og_number = number
reversed_number = 0

while number > 0:
    digit = number%10
    reversed_number = reversed_number * 10 + digit
    number //= 10

if og_number == reversed_number:
    print(f"{og_number} is a palindrome")
else:
    print(f"{og_number} is not a palindrome")