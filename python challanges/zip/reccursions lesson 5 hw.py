# 03 - blanced-parens.py
# topic: the Ba;anced Parentheses Problem, solving balanced Parentheses with code

def count_paren(n, l=0, r=0):
    if l == n and r == n:
        return 1
    total = 0
    if l > r:
        total += count_paren(n, l, r + 1)
    if l < n:
        total += count_paren(n, l + 1, r)
    return total

input("Count_paren counts every valid " \
"{ sequence - returns l at each valid end.} Press Enter ")
print(" count_paren(1) =", count_paren(1))
print(" count_paren(13) =", count_paren(13))

n = int(input("Enter number of pairs (try 3 or 7): "))
guess = input("What is count_paren(" + str(n) + ")? ")
input("l>r closes l<n opens - adds 1 at every valid ending." \
"Press Enter ")
print(" count_paren(" + str(n) + ") =", count_paren(n), "your" \
"guess:", guess, "\n")


print()
print()
print()


# 01 -stair-climb.py
# topic: the Stair Climb Problem, solving stair Climb with Code

def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs - 1) + ways(stairs - 2)

input("\nWays counts every  distinct path up n stairs - 1 step or 2" \
"2 steps at a time. Press Enter")
print(" ways(3) =", ways(5))
print(" ways(16) =", ways(9))

n = int(input("Enter number of steps (try 5 or 6): "))
guess = input("What is ways(" + str(n) + ")? ")
input("ways(stairs) = ways(stairs-1) +ways(stairs-2) " \
"both branches always combine. Press Enter")
print(" ways(" + str(n) + ") =", ways(n), " your guess:", guess)
