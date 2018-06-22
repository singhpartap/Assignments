#Q1
#Solution:

class Animal :
	def animal_attribute(self):
		print("Animals")
		return self.display()
		
class Tiger(Animal):
	def display(self):
		print("Tiger")
	
s=Tiger()
s.animal_attribute()
s.display()


#Q2
#Solution:
#A,B
#A,B


#Q3
#Solution:

class cop:
    def __init__(self, name, age, work_experience, designation):
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.designation = designation

    def display(self):
        print("Details:")
        print(self.name)
        print(self.age)
        print(self.work_experience)
        print(self.designation)

    def update(self, name, age, work_experience, designation):
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.designation = designation

class Mission(cop):
    fighter_planes = 10
    tankers = 3

    def add_mission_details(self):
        print("number of fighter planes:", self.fighter_planes)
        print("number of tankers:", self.tankers)

name = input("Name:")
age = int(input("Age:"))
work_experience = input("Work Experience:")
designation = input("Designation:")

a = Mission(name, age, work_experience, designation)
print("")
a.display()
print("")
a.add_mission_details()
print("")
a.update(input("Name:"), int(input("Age:")), input("Work Experience:"), input("Designation:"))
print("")
a.display()


#Q4
#Solution:

class Shape:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	
	def area(self):
		self.area=self.length*self.breadth
		
			
class Square(Shape):		
	def show(self):
		
		print("Area of square is",self.area)
		
class Rectangle(Shape):
	def display(self):
	
		print("Area of rectangle is",self.area)
	
length=int(input("Enter the length :"))
breadth=int(input("Enter the breadth:"))

x=Square(length,breadth)

y=Rectangle(length,breadth)
if length==breadth :
	print("The given parameters are of square.")
	x.area()
	x.show()
else:
	print("The given parameters are of rectangle.")
	y.area()
	y.display()




