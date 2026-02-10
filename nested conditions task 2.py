#Take input of number of units consumed by the user
units = int(input("Please enter the number of units you consumed: "))

#check conditions of units consumed
#Then vcalculate amount and surcharge accordingly
#surcharge is in the tax value

#check for units less than or equal to 50
if (units <= 50):
    amount = units * 2.60
    surcharge = 25

#check for units less than or equal to 100
elif (units <= 100):
    amount = 230 + ((units-50) * 3.25)
    surcharge = 35

#check for units less than or equal to 200
elif (units <= 100):
    amount = 130 + 162.50 + ((units-100) * 5.26)
    surcharge = 45
    
#check for all the cases other than mentioned
#when units consumed are more than 200
else:
    amount = 130 + 162.50 + 526 +((units-200) * 8.45)
    surcharge = 75

# calculate and display the total electricity bill
#total amount = amount + surcharge
total_amount = amount + surcharge
print("\nElectricity Bill = %.2f" %total_amount)