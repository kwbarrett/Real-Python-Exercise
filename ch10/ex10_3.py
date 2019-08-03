class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


class MiniaturePoodle(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


shape = Rectangle(5,4)
print(f"The area of your shape is {shape.area()}")

shape2 = Square(4)
print(f"The area of your shape is {shape2.area()}")

