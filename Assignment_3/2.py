l1=list(range(1,11))             #a03p02a.py
print(l1)

l2=list(range(10,101,10))        #a03p02b.py
print(l2)

                                 #a03p02c.py
l3=["python","django","flask","string","function","classes"]  
print(l3)

l4={"l1":l1,"l2":l2,"l3":l3}     #a03p02d.py
print(l4)

main_list=[]                     #a03p02e.py
main_list.extend(l1)
main_list.extend(l2)
main_list.extend(l3)
print "main list is:-",main_list

l5=l1*2                          #a03p02f.py
print(l5)  

main_list.append(l5)             #a03p02g.py
print(main_list)                           

                                 #a03p02h.py
print "occurance of 1 in main list is:-",main_list.count(1)



