class Ferrari():
    def fuel_type(self):
        print("Petrol -")

    def max_speed(self):
        print("Max speed of 350km/h")

class BMW():
    def fuel_type(self):
        print("Diesel -")

    def max_speed(self):
        print("Max speed of 240km/h")

ferrari = Ferrari()
bmw = BMW()

for car in (ferrari, bmw):
    car.fuel_type()
    car.max_speed()