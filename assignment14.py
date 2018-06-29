#Q1
#Solution:
f=open('demo.txt','r')

print("To print last 'n' lines.")

content=f.readlines()

#To print lines using loop.
lines=int(input("Enter the number of line from ending:"))
i=-lines
while i<=-1:
	print(content[i])
	i=i+1
	
f.close()



#Q2
#Solution:



words=open("demo.txt","r",encoding="utf8").read().split()
print(words)
print(type(words))
uniqWords=sorted(set(words))
print(type(uniqWords))
for word in uniqWords:
 print(words.count(word),word)

#Q3
#Solution:


with open('demo.txt','r') as f1:
	with open('test.txt','w') as f2:
		for line in f1:
			f2.write(line)
			
			
#Q4
#Solution:

with open('demo.txt','r') as f1:
	with open('test.txt','r') as f2:
		for line1,line2 in zip(f1,f2):
			print(line1+line2)
			
			
			
			
#Q5
#Solution:



import random

with open("demo.txt", "w") as f:
    for i in range(10):
        numbers = str(random.randint(1, 100))
        f.writelines(numbers + '\n')
        print(numbers)

with open("demo.txt") as f1, open("test.txt", "w") as f2:
    numbers = f1.read().split()
    numbers.sort()
    print(numbers)
    for n in numbers:
        f2.write(n)
        f2.write("\n")