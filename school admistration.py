class Student:

	def __init__(self, name, rollno, number, CGPA):
		self.name = name
		self.rollno = rollno
		self.number = number
		self.CGPA = CGPA


	def accept(self, Name, Rollno, number, CGPA):
		ob = Student(Name, Rollno, number, CGPA)
		ls.append(ob)

	def display(self, ob):
		print("Name : ", ob.name)
		print("RollNo : ", ob.rollno)
		print("NUMBER : ", ob.number)
		print("CGPA : ", ob.CGPA)
		print("\n")

ls = []
obj = Student('', 0, 0, 0)

obj.accept("rahul", 1234, 1234567890, 7)
obj.accept("kamal", 2345, 2345678901, 9)
obj.accept("vikas", 3456, 4567890123, 6)


print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
	obj.display(ls[i])

print("Thank You !")
