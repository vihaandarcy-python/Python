class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):

        return self.word+' ( '+self.meaning+' )'
    
flash = []
print('Welcome to flshcard application')

while(True):
    word = input("Enter the name of your flash card: ")

    meaning = input("Enter the meaning of your word: ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0, if you want to add another flashcard otherwise enter 1 : "))

    if (option):
        break

print("\nYour flashcards")
for i in flash:
    print(">", i)



