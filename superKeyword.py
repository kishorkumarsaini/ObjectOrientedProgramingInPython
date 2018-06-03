#!/usr/bin/python3

class Person:
    name=""
    age=0
    def __init__(self,Person_name,Person_age):
        self.name=Person_name
        self.age=Person_age
    def show(self):
        print("Name=",self.name)
        print("Age=",self.age)
class Student(Person):
    Student_id=0
    def __init__(self,Student_name,Student_age,Student_id):
        self.Student_id=Student_id
        super().__init__(Student_name,Student_age)
        #Person.__init__(self,Student_name,Student_age)
    def showId(self):
        super().show()
        print("Student id=",self.Student_id)


s=Student("kishor",21,23599)
s.showId()
#s.show()
