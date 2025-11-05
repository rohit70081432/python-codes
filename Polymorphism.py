class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.speak() 
