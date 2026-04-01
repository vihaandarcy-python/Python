test_dict = {'codingal' :1, 'is':2, 'best':3, 'for':2, 'coding':1, ',':7, 'this':7, 'is':9, 'a':10, 'task':5, 'for':5, 'coding':6}

print("The origional dictionary : " + str(test_dict))

k = int(input("Enter your favourate number: "))

res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

print("Frequency of K is: " + str(res))
