setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Origional set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
setz1 = sety.difference(setx)
setz2 = setx.difference(sety)
setz3 = setx.symmetric_difference(sety)
print(setz)
print(setz1)
print(setz2)
print(setz3, '\n')

print("Unique elements in set: ")
setz4 = setx.union(sety)
print(setz4)