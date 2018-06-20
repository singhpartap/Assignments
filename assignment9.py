#Q1:
#Solution:

class circle :
    def __init__(self,radius):
      self.r =radius
    def area(self):
        print("Area of circle is :",3.14*self.r**2)
    def cicumference(self):
        print("Circumference of cicle is :",2*3.14*self.r)
s=circle(int(input("Enter radius of circle:")))
s.area()
s.cicumference()


#Q2
#Solution:

class student:
    def __init__(self,name,roll):
        self.n=name
        self.r=roll
    def display(self):
        print("Name of student is %s\nRoll number of %s is %d"%(self.n,self.n,self.r))
s=student(name=str(input("Enter student name:")),roll=int(input("Enter student roll number:")))
s.display()


#Q3
#Solution:

class Temperature:
    def __init__(self,celsius,fahrenheit):
        self.c=celsius
        self.f=fahrenheit
    def fahr(self):
        f=9/5*self.c+32
        print("Temperature in Fahrenheit scale is %dF."%f)
    def cels(self):
        c=(self.f-32)*5/9
        print("Temperature in celsius scale is %dC."%c)
s=Temperature(celsius=int(input("Enter the temperature in celsius:")),fahrenheit=int(input("Enter the temperature in fahrenheit:")))
s.fahr()
s.cels()


#Q4
#Solution:

class Movie_Detail:
    def __init__(self,name,artist,release,rating):
        self.name=name
        self.artist=artist
        self.release=release
        self.rating=rating

    def display(self):
        print("Name of movie is %s.\nRole played by %s.\nDate of release is %s.\nRatings:%s."%(self.name,self.artist,self.release,self.rating))
    def update(self):
        self.name=input("Latest movie name:")
        self.artist=input("Name of artist:")
        self.release=input("Date of release:")
        self.rating=input("ratings")

s=Movie_Detail(name=input("Enter the name of movie:"),artist=input("Enter the name of artist:"),release=input("Enter the date of release"),rating=input("Enter the ratings:"))
s.display()
s.update()
s.display()

#Q5
#solution:


class Expenditure:
    def __init__(self,expend,saving):
        self.expend=expend
        self.saving=saving
    def display(self):
        print("You spend RS%d per month.\nAnd your saving is Rs%d."%(self.expend,self.saving))
    def total(self):
        self.expend+self.saving
    def display_salary(self):
        print("Your total salary is Rs%d"%(self.expend+self.saving))
s=Expenditure(expend=int(input("Enter your total monthly expenditure in INR:")),saving=int(input("Enter your monthly saving in INR:")))
s.display()
s.total()
s.display_salary()