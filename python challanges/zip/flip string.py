def flip_word(s):
    if len(s) == 1:
        return s
    return flip_word(s[1:]) + s[0]

input("flip_word recurses on s[1:] then attaches s[0] at the end. Press Enter")
print("  Flip_word('GiRRafE') =", flip_word('GiRRafE'))
print("  Flip_word('table') =", flip_word('table'))


word = input("Enter a word(try  a name or 'laptop')")
guess = input("What is the flip_word of('" + word + "')? ")
input("flip_word(s) = flip_word(s[1:]) +s[0] first character lands last. Press Enter")
print(" flip_word('" + word + "') =", flip_word(word), "your guess:", guess)