#!/usr/bin/python3

class Person:
    def __init__(self,Person_name,Person_age):
        self.name=Person_name
        self.age=Person_age
    def show(self):
        print("Name=",self.name)
        print("Age=",self.age)
class Student:
    def __init__(self,Student_id):
        self.Student_id=Student_id
    def showId(self):
        print("Student_id=",self.Student_id)

class Resident(Person,Student):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        Student.__init__(self,id)


r=Resident("kishor",21,23599)
r.show()
r.showId()
