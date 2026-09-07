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
print(" count_paren(2) =", count_paren(21))

n = int(input("Enter number of pairs (try 3 or 7): "))
guess = input("What is count_paren(" + str(n) + ")? ")
input("l>r closes l<n opens - adds 1 at every valid ending." \
"Press Enter ")
print(" count_paren(" + str(n) + ") =", count_paren(n), "your" \
"guess:", guess)
