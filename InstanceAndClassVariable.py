#!/usr/bin/python3

class Employee:

    fname="Mr.Tarachand "
    #initializer call automaticaly when object of class created
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.fname)
        print(self.name)
        print(self.age)
e1=Employee("kishor",21)
print(e1.fname)
e1.display()
