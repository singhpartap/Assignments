#NOTE : List is mutable 
#       Tuple are immutable
#       Strings are immutable




#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1


print (L[2])





#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

L[2]=8
print (L)





#list 

L=['a',2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

L[0]=input("enter value :")
print (L)






#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1


print (L[1:3])







#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1


print (L.append(6))
print(L)







#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1
#NOTE :  Strings are immutable
#Mutable means can be modified
#immutable means cannot be modified
x='abc'
print(x.upper())








#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

# when we use insert function then remaining values shift

print (L.insert(2,'b'))
print(L)







#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

L2=[6,7,8]

print (L.extend(L2))
print(L)







#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

#in this value is directy given
print (L.index(3))






#list 

#L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

x="abc"
print (x.find("b"))





#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

#in this value is directly given
print (L.remove(2))
print(L)





#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

#in this position is give to the function
del L[3]
print(L)




#list 

L=[6,5,8,7,9]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

L.sort()
print (L)




#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

L.reverse()
print (L)




#list 

L=[7,5,6,8,4]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

L.sort()
L.reverse()
print (L)





#list 

L=[1,2,3,4,5]
#  0,1,2,3,4
# -5,-4,-3,-2,-1


print (L.pop())
print(L)






#list 

L=[1,2,1,4,1]
#  0,1,2,3,4
# -5,-4,-3,-2,-1


print (L.count(1))









#list 

L=[[1,2,3,4,5],[6,7,8,9]]
#  0,1,2,3,4
# -5,-4,-3,-2,-1


print (L)









#list 

l=[1,2,3]

L=[l,[6,7,8,9]]
#  0,1,2,3,4
# -5,-4,-3,-2,-1


print (L)






#list 

L=[[1,2,3,4,5],[6,7,8,9]]
#  0,1,2,3,4
# -5,-4,-3,-2,-1

#to print directly particular element in 2D array
print (L[1][2])






#Tuple
t=(1,2,3,4)

print(t[2])
print(t[1:3])






#Tuple
t=(1,2,3,4)


print(max(t))

print(min(t))

print(len(t))






#Tuple
t=(1,2,3,4)
 
 
 # to delete tuple
del (t) 






#Tuple
t=(1,2,3,4)

l=[6,7,8,9]

t2=list(t)
l2=tuple(l)

print(t2)

print(l2)
 
 
