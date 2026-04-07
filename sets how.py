setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Origional set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz2 = sety.difference(setx)
setz3 = setx.difference(sety)
setz4 = setx.symmetric_difference(sety)
print(setz2)
print(setz3)
print(setz4, '\n')

print("Unique elements in set: ")
setz1 = setx.union(sety)
print(setz1)