
def hcf(numberSmallest, numberLargest):
    while(numberSmallest):
        numberStore = numberSmallest
        numberSmallest = numberLargest % numberSmallest
        numberLargest = numberStore
    return numberLargest


numberLargest = int(input("Enter the larger number: "))
numberSmallest = int(input("Enter the smaller number: "))


lcm = int((numberSmallest / hcf(numberSmallest, numberLargest)) * numberLargest)
print("LCM is : ", lcm)
print("HCF is: ", hcf(numberSmallest, numberLargest))