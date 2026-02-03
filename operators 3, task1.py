#identity operators(is and isnot operators)

x=5
if(type(x) is int):
    print("true")
else:
    print("flase")

x= 5.5
if(type(x) is float):
    print("true")
else:
    print("flase")

x=20
y=20

if (x is y):
    print("x & y are the same identity")

y += 10
if (x is not y):
    print("x & y have different identity")