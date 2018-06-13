#Q1
a=input("enter value")
b=input("enter value")
c=input("enter value")
d=input("enter value")
e=input("enter value")
l = [a,b,c,d,e]
print(l)


#Q2:

l2=['google','apple','facebook','microsoft','tesla']

print(l.extend(l2))

print(l)


#Q3

l=[1,2,3,1,4,1,5,1]

print(l.count(1))




#Q4

l=[33,11,66,44,22]

l.sort()

print(l)





#Q5
A=[1,2,3,7,10]
B=[5,6,8,9]
print(A.extend(B))
C=A
C.sort()
print(C)




#Q6
#For Stack

a=input("enter value")
b=input("enter value")
c=input("enter value")
d=input("enter value")
e=input("enter value")
l = [a,b,c,d,e]
print(l.pop())
print(l)


#For Queue


a=input("enter value")
b=input("enter value")
c=input("enter value")
d=input("enter value")
e=input("enter value")
l = [a,b,c,d,e]

l.reverse()
print(l.pop())

print(l)