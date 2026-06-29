
n = 4
print("==== Counting Game Points (n=", n, "rounds) ====")
print()


#Steps = 1 (psuedocode)
total = n * (n-1) // 2
print("Formula way : total =", total, "| steps = 1")

#steps = 2(Loop way) - n steps

total = 0
steps = 0
for round_num in range(1, n +1):
    total += round_num
    steps += 1
print("Loop way  : total =", total, "| steps =", steps)


#steps = 3( Nested Loop way) - roughly n^n steps

total = 0
steps = 0
for round_num in range(1, n+1):
    for point in range(1, round_num + 1):
        total += 1
        steps += 1
print("Nested loop : total=", total, "| steps =", steps)


n = 10
nested_steps = 0
for round_num in range(1, n+1):
    for point in range(1, round_num+1):
        nested_steps += 1

print()
print("=== Now with n =", n, "rounds ===")
print("Formula way  : steps = 1           (always just 1!)")
print("Loop way     : steps =", n)
print("Nested loop  : steps =", nested_steps, "(grows much faster!)")
print()
print("Same answer - but very different costs, That is time complexity")

