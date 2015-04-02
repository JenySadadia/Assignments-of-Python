Gender=str(input("Enter the gender of an employee."))
CurrentSalary=int(input("Enter the Current Salary of an employee.")) 

if((CurrentSalary<1000 and Gender=='male')==True):
	bonus=(CurrentSalary*5)/100
	print("bonus is :-",bonus)

elif((CurrentSalary<1000 and Gender=='female')==True):
	bonus=(CurrentSalary*5.5)/100
	print("bonus is :-",bonus)

elif(CurrentSalary>1000):
	bonus=(CurrentSalary*5)/100
	print("bonus is :-",bonus)