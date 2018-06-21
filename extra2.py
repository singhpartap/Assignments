#In case of female we use 'l_age' function to take female age for enrolment.
def lady_age(l_age):
	#For checking input age  is correct or numerical. 
	if l_age.isdecimal():
		#To convert age input into numerical value.
		l_age=int(l_age)
		#for checking eliginility criteria using below conditions.
		if l_age>=19 :
			print("Congartulation mam you are elligible to enrol 'PYTHON' course.")
			
		#If conditionis false or age is below than elligibility criteria age.
		else:
			print("Sorry mam as your age is below to elligibility criteria age.\nYou can\'t enrol for 'PYTHON' course")
	#If input is incorrect.
	else:
		print("Mam,Please enter appropriate value. ")
	# After incorrect input recall 'lady_age' function.
		lady_age(l_age=input("Mam, Please enter your age:"))
		
	
	
#In female case for taking name as input using 'lady_name' function after entering gender.		
def lady_name(l_name):
#For checking lady name input is coorect or not.
	if l_name.isalpha():
	#When condition is true we recall 'lady_age' function.
		lady_age(l_age=input("Mam, Please enter your age:"))
		
		
	#When condition is false then recall 'lady_name' function.	
	else:
		print("Mam, Please enter appropriate value.")
		lady_name(l_name=str(input("Mam, Please enter your name:")))

	
	
#If gender is male  and after input the name using below function.
def man_age(m_age):
	#for checking age is decimal or not. 
	if m_age.isdecimal():
	#If age is decimal  then convert decimal age into numerical value.
		m_age=int(m_age)
	#After this we checking elligibility criteria age.
		if m_age>=20:
			print("Congartulation sir you are elligible to enrol 'PYTHON' course.")
		#If age is below elligibility criteria age print below message.
		else:
			print("Sorry sir as your age is below to elligibility criteria age.\nYou can\'t enrol for 'PYTHON' course.")
	#If input age is incorrect recall 'man_age' function.
	else:
		print("Sir,Please enter appropriate value. ")
		man_age(m_age=input("Sir,Please enter your age:"))
				

				
#If gender is male using below function.
def man_name(m_name):
#for check man name is correct or not.
	#If input is correct call 'man_age' function.
	if m_name.isalpha():
		man_age(m_age=input("Sir,Please enter your age:"))

	#If input is incorrect, again call man_name function.
	else:
		print("Sir,Please enter appropriate value. ")
		man_name(m_name=str(input("Sir, Please enter your name:")))
		
		

#For gender input using below function.
def gender(gen):
	#To check gender is male or female or input is correct.
	if gen=='m' or gen=='male':
	#If gender is male we call 'man_name' function.
		print("Hello Sir, Welcome to our python tutorials.")
		print("Sir we want to know your real name and age for Enrolment.")
		man_name(m_name=str(input("Sir, Please enter your name:")))
	#If gender is female we call 'lady_name' function.
	elif gen=='f' or gen=='female':
		print("Hello Mam, Welcome to our python tutorial.")
		print("Mam we want to know your real name and age for Enrolment.")
		lady_name(l_name=str(input("Mam, Please enter your name:")))
		
	#If input is incorrect call 'gender; function again.
	else:
		print("Sir,Please enter appropriate value. ")
		gender(gen=str(input("Enter your gender:")))

		
		
#To call gender function and start program.		
gender(gen=str(input("Enter your gender:")))


