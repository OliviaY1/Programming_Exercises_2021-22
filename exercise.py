#

class Vehicle():
    def __init__(self, name = None, max_speed = None, capacity = None):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity

    def vroom(self) -> None:
        # print 'vroom' max_speed times
        print('Vroom ' * self.max_speed)

class Bus(Vehicle):
    def __init__(self):
        super().__init__()

    def fare(self, age:float) -> None:
        if 17 >= age >=0 :
            print(f"The fare of the bus ride is Free")
        elif 60>= age >= 18:
            print(f"The fare of the bus ride is $5")
        else:
            print(f"The fare of the bus ride is Free")

a = Bus()
a.fare(20)

b = Vehicle('Train', 10, 1000)
b.vroom()