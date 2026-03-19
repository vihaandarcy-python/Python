import math#using ceil and floor function of the math module
print("The floor and ceiling value of 24.56 are: " + str(math.ceil(24.56)) + ', ' + str(math.floor(24.56)))

x = 10
y = -15
#using the copysign function
print("The value of X after copying the sign from Y is: " + str(math.copysign(x,y)))

#using Fabs and gcd functions
print("Absolute value of -96 and 56 are: " + str(math.fabs(-96)) + ', ' + str(math.fabs(56)))

print("The GCD 24 and 56 :" + str(math.gcd(24, 56)))