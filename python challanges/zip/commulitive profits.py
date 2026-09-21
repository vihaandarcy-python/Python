def total_ptofits(n):
    prices = [1, n, 1, n, 1]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices [i - 1]:
            profit += prices[i] - prices[i - 1]
        return profit

input("Total_progit(n) sums every upswing in prices "
"[1, n, 1, n, 1]. Press Enter")
print("   total_profit(4) =", total_ptofits(4))
print("   total_profit(5) =", total_ptofits(5))
n = int(input("Enter n (try 6 or 7): "))
guess = input("What is total_profit(" +str(n) + ")? ")
input("Add every positive step - two peaks each contributet" \
"n -1. Press Enter")
print("  total_ptofit(" + str(n) + ") =", total_ptofits(n), " "
"your guess: ", guess)