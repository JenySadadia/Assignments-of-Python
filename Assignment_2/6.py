l=['mercury','venus','earth','mars','jupitor','saturn','uranus','neptune']
planet=input("Enter the name of planet.")

for i in range(0,4):
    if planet==l[i]:
        print("Its a inner planet which you have choosen.")
        ch=input("If you want to continue press Y otherwise N.")
        if ch=='Y':
        	continue
        else:
        	break	
        
      
for i in range(4,8):
    if planet==l[i]:
        print("its a outer planet which you have choosen.")
        ch=input("If you want to continue press Y otherwise N.")
        if ch=='Y':
        	continue
        else:
        	break	
        
        
    else:
        print("Enter proper choice.")
        ch=input("If you want to continue press Y otherwise N.")
        if ch=='Y':
        	continue
        else:
        	break	
        
         
