#!/usr/bin/python3

class Employee:

    def Registration(self,name,age):
        self.name=name
        self.age=age
        print("Name=",self.name)
        print("Age=",self.age)
    @staticmethod
    def welcome(Age):
        print("hello welcome to comming this class")
        print(Age)
e1=Employee()
e1.Registration("kishor",21)
Employee.welcome(32)
