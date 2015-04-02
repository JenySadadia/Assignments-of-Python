
while True:
    op=input('''Enter the operation which you would like to b performed :-
    1.Enter + foraddition
    2.Enter - for subtraction
    3.Enter * for multiplication
    4.Enter / for division
    5.Enter % for modulo .''')


    if op=='+':
        x=int(input("enter x")) 
        y=int(input("enter y"))
        print(x+y)
        
    	
    
    elif op=='-':
        x=int(input("enter x")) 
        y=int(input("enter y"))
        print(x-y)
       
    
    elif op=='*':
        x=int(input("enter x")) 
        y=int(input("enter y"))
        print(x*y)
        
 
    elif op=='/':
        x=int(input("enter x")) 
        y=int(input("enter y"))
        print(x/y)
    
    elif op=='%':
        x=int(input("enter x")) 
        y=int(input("enter y"))
        print(x%y)


    else:
        print("invalid choice")
        
        
    