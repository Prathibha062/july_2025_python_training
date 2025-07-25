class Vehicle:
    def move(self):
        print("moving")
class Car(Vehicle):
    def wheels(self):
        print("4 wheels")
c=Car()
c.move()
c.wheels()