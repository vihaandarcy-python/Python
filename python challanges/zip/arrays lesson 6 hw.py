# 01-eq-mid.py
#Topics: slices and their sums, Left-right balance, equibibroum point



def eq_mid(n):
    arr = [1]*n + [0] + [1]*n
    size = len(arr)
    for i in range(size):
        left_sum = 0
        right_sum = 0
        for j in range(i):
            left_sum += arr[j]
        for k in range(i + 1, size):
            right_sum += arr[k]
        if left_sum == right_sum:
            return i
    return "Array does not hold a equiblirium point!"

n = int(input("Enter n (try 8 or 9): "))
guess = input("What is eq_mid(" + str(n) + ")? ")
print("  eq_mid(" + str(n) + ") =", eq_mid(n), "  your guess:", guess)



#-------{[[[[[[[[[[[["""____"""]]]]]]]]]]]]-------}





# 02-eq-val.py
# Topic: Slices and their sums, Equilibrium point

def eq_val(n):
    arr = [3]*n + [n]*4 + [1]*n
    size = len(arr)
    for i in range(size):
        left_sum = 0
        right_sum = 0
        for j in range(i):
            left_sum += arr[j]
        for k in range(i + 1, size):
            right_sum += arr[k]
        if left_sum == right_sum:
            return arr[i]
    return "Array does not hold a equiblirium point!"

n = int(input("Enter n (try 8 or 614): "))
guess = input("What is eq_val(" + str(n) + ")? ")
print("  eq_val(" + str(n) + ") =", eq_val(n), "  your guess:", guess)





#-------{[[[[[[[[[[[["""____"""]]]]]]]]]]]]-------}





#03-win-sum.py
#Topic: Subarray window, target sum search

def win_sum(n):
    arr = [1]*n + [2]*n
    size = len(arr)
    for i in range(size - n + 1):
        curr_sum = 0
        for j in range(i, i+n):
            curr_sum += arr[j]
        if curr_sum == n:
            return i

    return "Array does not hold a equiblirium point!"


n = int(input("Enter n (try 8 or 9): "))
guess = input("What is win_sum(" + str(n) + ")? ")
print("  win_sum(" + str(n) + ") =", win_sum(n), "  your guess:", guess)