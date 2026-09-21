# 01-max profits.py
# Topic: stocks vuy-sell

def max_profits(n):
    prices = list(range(n, 0, -1)) + list(range(1, n + 1))
    min_price, profit = prices[0], 0
    for p in prices[1:]:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit

input("Max_profit(n) finds the best single buy-sell in prices" \
"[n..1, 1...n]. Press enter")
print("Max_profit(4) =", max_profits(4))
print("Max_profit(5) =", max_profits(5))
n=int(input("Enter n(try 6 or 7): "))
guess = input("What is max_profit(" + str(n) + ")? ")
input("Track min price so far- sell when the " \
"gap beats the current best. Press Enter")
print("   max_profit(" + str(n) + ") =", max_profits(n), "your guess:", guess)