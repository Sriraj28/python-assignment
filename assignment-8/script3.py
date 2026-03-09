class Car:
    def move(self):
        print("Driving on the road")

class Bicycle:
    def move(self):
        print("Pedaling on the road")

def start(vehicle):
    vehicle.move()

start(Car())
start(Bicycle())