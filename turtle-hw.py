import turtle
#inport the turtle library
turtle.Screen().bgcolor("Yellow")
turtle.Screen().setup(300,400)
Square = turtle.Turtle()

num_sides = 4 #variable
side_length = 120 
angle = 360.0/ num_sides
#iterate loop for total number of side
for i in range(num_sides):
    Square.forward(side_length)
    Square.right(angle)

turtle.done()