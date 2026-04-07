import array as arr
#create an array
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])

#count number of occurances
print("Number of occurances of the number 3 in the said array: " + str(array_num.count(3)) + '\n') 

#reverse the array
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))