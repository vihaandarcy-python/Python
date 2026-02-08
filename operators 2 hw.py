print("Enter a character: ")
c = input()
if c>'0' and c <='100':
    print("\nIt is an number")
if c>'a' and c <='z':
    print("\nIt is an number")
if c>'A' and c <='Z':
    print("\nIt is an Alphabet")

else:
    print("\n It is not an alphabet nor an number!")