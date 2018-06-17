#Problem:
#Solution:

# for taking name as a input.
name=input("what is your name?:")

#for taking age as a input.
age=int(input("what is your age?"))

#for calculating the year in which userage is 100.
if age<100:
    remain=2018+(100-age)
    print("hello",name )
    print("your age is",age)
    print("and you become 100 year old at",remain)
#if person is already 100.
else:
    x=2018-(age-100)
    print("hello",name)
    print("your age is",age)
    print("you are age is already 100 at ",x)
	
	
	
	
#Question:
#solution:

#make a list to represent numbers in a single line and separated by comma(,).
l=[]
#for series.
for number in range (2000,3200):
    #logic of number divisible by 7 but not a multiple of 5.
    if number%7==0 and number%5!=0:
        l.append(number)
print(l)




#Bonus Question:
#Solution:


x=input("write a sentence:")
y=0
z=0
#To traverse in sentence.
for i in x:
#To calculate upper case word.
    if i.isupper():
        y=y+1
#To calculate lower case word.
    elif i.islower():
        z=z+1
print("Number of UPPER CASE are:" ,y)
print("Number of LOWER CASE:",z)




#Question:
#Solution:


s=input("enter:")
l=s.split(',')
t=tuple(l)
print(l)
print(t)