class Student():
	def __init__(self, name, age, ID, yr = "First Year"):
		self.name = name.title()
		self.age = age
		self.ID = ID
		self.yr = yr
  
	def printInfo(self):
		print(f"Name:- {self.name}\nAge:- {self.age}\nID:- {self.ID}\nYear:- {self.yr}")
  
	def YearsToHundred(self):
		print(self.name, "has ", 100-self.age, "years to become 100.")
    
	def go_to_school(self):
		print(f"{self.name} is going to college.")
		
	def study(self):
		print(f"{self.name} is studying now.")
		
student1 = Student("aritra mukhopadhyay", 19, "2011030")
student1.printInfo()
student1.YearsToHundred()
student1.go_to_school()
student1.study()
