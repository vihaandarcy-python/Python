import turtlea # importing library

# Create screen
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")

# Create turtle
my_pen = turtle.Turtle()

size = 0

while True:  # infinite loop
    for i in range(4):  # draw 4 sides (square)
        my_pen.forward(size + 1)
        my_pen.left(90)
        size = size - 5   # decrease size slightly each side
    
    size = size + 1  # increase size after each square