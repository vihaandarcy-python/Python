# 01 -stair-climb.py
# topic: the Stair Climb Problem, solving stair Climb with Code

def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs - 1) + ways(stairs - 2)

input("Ways counts every  distinct path up n stairs - 1 step or 2" \
"2 steps at a time. Press Enter")
print(" ways(3) =", ways(3))
print(" ways(16) =", ways(16))

n = int(input("Enter number of steps (try 5 or 6): "))
guess = input("What is ways(" + str(n) + ")? ")
input("ways(stairs) = ways(stairs-1) +ways(stairs-2) " \
"both branches always combine. Press Enter")
print(" ways(" + str(n) + ") =", ways(n), " your guess:", guess)

