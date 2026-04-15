class Greyhounds:

    species = "Mammal"
    Movement = "4 limbs."

    def __init__(self, Breed, Speed):
        self.Breed = Breed
        self.Speed = Speed 

Alan = Greyhounds("Greyhound", "45km/h")
Mike = Greyhounds("Afghani_Greyhound", "42km/h")

print("Alan is a {} who walks on {}".format(Alan.species, Alan.Movement))
print("Mike is also a {} who walks on {}".format(Alan.species, Alan.Movement))

print("\nAlan is a {} who's speed is {}".format(Alan.Breed, Alan.Speed))
print("Mike is a {} who's speed is {}".format(Mike.Breed, Mike.Speed))
