try:
    num1, num2 = eval(input("Enter two numbers, sperated by a comma : "))

    result = num1 / num2
    print("Result is: ", result)
#using multiple except blocks for different typw of error 

except ZeroDivisionError:
    print('Division by zero is error!!')

except SyntaxError:
    print(" Comma is missing. Enter numbers seperatated by \
    comma like this 1, 2")
    
except: 
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")