#input a word
text = str(input("Enter a string: "))

#reverse string
#using step value as -1 to iterate in reverse

revText = text[::-1]
text = revText

print("reverse if the given string is: ")
print(text)