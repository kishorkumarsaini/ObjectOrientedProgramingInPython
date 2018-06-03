#!/usr/bin/python3

class Employee:
	name="kishor"
	desigation="sales Executive"
	salesMadeThisWeek=6

	def hasAchieveTareget(self):
		if self.salesMadeThisWeek >=5:
			print("Target has been achive")
		else:
			print("Target has not been achive")

e1=Employee()
e1.name
print(e1.name)
e1.hasAchieveTareget()