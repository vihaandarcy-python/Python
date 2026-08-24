#RECURSION PATTERNS
# Topics: Linear | Tail | Head | Increasing-Deacreasing | Tree 


# PART 1: Linear Recursion - one call per level, one path down
def linear(n):
    if n == 0:
        return
    print(n, end=" ")
    linear(n-1)

print("Linear recursion (one call per level):")
linear(5)
print()


# PART 2: Tail Recursion - call is LAST, work goes down
def tail(n):
    if n == 0:
        return
    print(n, end=" ")
    tail(n-1)

print("Tial recursion (prints going down):")
tail(5)
print()


# PART 3: Head Recursion - call is FIRST, work comes Up  only
def head(n):
    if n == 0:
        return
    head(n-1)
    print(n, end=" ")

print("Head recursion (prints coming up):")
head(5)
print()

# PART 4:
#Increasing-Decreasing - work on BOTH sides of thecall
def inc_dec(n):
    if n == 0:
        return
    print(n, end=" ")
    inc_dec(n-1)
    print(n, end=" ")

print("Increasing -Decreasing (down and then up):")
inc_dec(4)
print()


#PART 5: Tree Recursion Two calls per level, branched double
def tree(n):
    if n == 0:
        return
    print(n, end=" ")
    tree(n-1)
    tree(n-1)

print("Tree recursion (two calls -- branches doublw:)")
tree(3)
print()
print("Level calls: 1 -> 2 -> 4 -> 8   (double every level!)")
