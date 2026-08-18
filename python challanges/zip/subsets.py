#Topics: Power Set | Binary Mask | Bit Probe | Subset |
#Enumeration | Bit Difference

items = ["A", "B", "C"]
n = len(items)
total = 2 ** n

print("=== Power Map ===")
print("Items:", items)
print("Elements:", n, " Total subsets : 2 ^", n, "=", total)
print()


# PART 1: Binary Mask Table
# Each number from 0 to (total -1) is a binary mask
# Bit position k = 1 means items[j] is IN the subset
print("Mask Table (n =", n, "):")
mask = 0
while mask < total:
    bit2  = (mask >> 2) & 1
    bit1 = (mask >> 1) & 1
    bit0 = mask & 1
    print("mask", mask, "-> [C][B][A] =", bit2, bit1, bit0)
    mask = mask + 1
print()


# Part 2: Build each subset using a bit probe
# 1 << j makes a probe with only one bit j set
# mask and probe > 0 means bit j IS set in mask -> include items[j]
print("All subsets (bit probe):")
mask = 0
while mask < total:
    subset = []
    j = 0
    while j < n:
        probe = 1 << j
        if (mask & probe) > 0:
            subset.append(items[j])
        j = j + 1
    print(" mask", mask, "->", subset)
    mask  = mask + 1
print()

# Part 3: Bit Difference
# How many bit positions differ between two numbers?
# Extrat last bit of each with & 1, compare, then right shift both
def bit_diff(a, b):
    flips = 0
    while a > 0 or b > 0:
        last_a = a & 1
        last_b = b & 1
        if last_a != last_b:
            flips = flips + 1
        a = a >> 1
        b = b >> 1
    return flips

print("Bit Difference:")
print(" diff(17, 5) =", bit_diff(17, 5), " (17=10001, 5=0101)")
print(" diff(21, 118) =", bit_diff(21, 118), " (21=10101, 118=1110110)")
print(" diff(67, 67) =", bit_diff(67, 67), " (same -> 0)")