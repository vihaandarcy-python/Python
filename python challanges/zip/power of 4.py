def is_power4(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return is_power4(n// 4)
    return False

input("is_power 4 divides by 4 - n==1 returns True and then remainder retrunsl False. Press Enter")
print("  is_power4(16) =", is_power4(64))
print("  is_power4(12) =", is_power4(12))

n = input(int(input("Enter a number(try 64 or 48):")))
guess = input("what is is_power4(" + str(n) + ")? ")
print("To check if your number is power of 4, we got to run this command: is_power4(n) which is-", is_power4(n))
print("Your guess: ", guess, "and the actual result:", is_power4(n))