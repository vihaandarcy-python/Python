def multiple_tuple(nums):
    temp = list(nums)
    product = 1
    for x in temp:
        product *= x
    return product
    
nums = (4, 3, 2, 2, -1, 10)
print("Origional tuple: ")
print(nums)
print("Product - multiplying all the numbers of the said tuple:",multiple_tuple(nums))

nums = (2, 4, 8, 8, 3, 2, 9)
print("Origional tuple: ")
print(nums)
print("Product - multiplying all the numbers of the said tuple:",multiple_tuple(nums))