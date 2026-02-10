print("Select your ride: ")
print("1. Bike")
print('2. Car')

#take input of number 1 0r 2
#select your ride
choice = int(input('Enter your choice: '))

#user entering option 1
if( choice == 1 ): #condition 1 outer if statement
    print( "what type of bike? ")
    print("1.Scooty\n")
    print("2.Scooter\nr")

    #condition for selecting the type of bike
    choice2=int(input("Enter your choice2: "))
    if choice2==1: #inner if statement
        print("you have opted for the scooty")
    else:
        print("You have opted for the scooter")

#user entering option 2
elif( choice == 2 ): #condition 1 outer elif statement
    print( "what type of car? ")
    print("1.Sedan\n")
    print("2.XUV\n")

    #condition for selecting the type of bike
    choice3=int(input("Enter your choice2: "))
    if choice3==1: #inner if statement
        print("you have opted for the Sedan")
    else:
        print("You have opted for the XUV")     


else: #outer else statement
    print("Wrong choice!")