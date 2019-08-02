class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age, coat_color):

        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, miles):
        self.mileage = self.mileage + miles


philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")

blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.mileage:,} miles")

new_car = Car("black", 0)
new_car.drive(100)
print(f"The {new_car.color} car has {new_car.mileage} miles")
