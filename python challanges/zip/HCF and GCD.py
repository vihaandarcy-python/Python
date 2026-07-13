numberLargest = int(input("Enter the larger number: "))
numberSmallest = int(input("Enter the smaller number: "))


while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is : ", numberLargest)