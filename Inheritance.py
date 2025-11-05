# class Animal:
#     def speak(self):
#         print("Animal is making a sound")


# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# dog = Dog()
# dog.speak()  
# dog.bark()   


class Animal:
    def eat(self):
        print("Animal is eating")

class Mammal(Animal):
    def walk(self):
        print("Mammal is walking")

class Dog(Mammal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()   
dog.walk() 
dog.bark() 
