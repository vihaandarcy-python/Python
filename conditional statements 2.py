#profit and loss calculator

actual_cost = float(input(" Please enter the actual cost of the product: "))

sale_amount = float(input(" Please enter the sale amount: "))

if (sale_amount> actual_cost):
    amount = sale_amount-actual_cost
    print("Total Profit = {0}".format(amount))

else:
    print("No profit!!!")