#/usr/bin/python3
class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):
    def bark(self):
        print("barking")
        Animal.eat(self)
class BabyDog(Dog):
    def weeping(self):
        print("weeping")

b=BabyDog()
#b.eat()
b.bark()
b.weeping()
