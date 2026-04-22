class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self. mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 10
    
class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount
    
School_bus = Bus("School Volvo", "12 Km", 50)
print("Total Bus fare for the trip is:", School_bus.fare())
