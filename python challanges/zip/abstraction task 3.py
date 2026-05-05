class India():
    def capital(self):
        print("New delhi is the capital of India.")

    def language(self):
        print("Hindi is the widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washigton, D>C. is the capital of USA")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USa is a developed country.")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()