import math

radius = float(input("Please enter the radius of your circle: "))

circ = 2 * math.pi * radius

def circumfurance():
    print("The circumfurance of your circle will is %0.2f" % circ)

circumfurance()