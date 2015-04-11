l=[2,5,'a',[1,'home',9],7,'j']

d={"bvng":"GJ4","abd":"GJ1","baroda":"GJ6"}

mainlist=[]
mainlist.append(l)
mainlist.append(d)
print(mainlist)

for k in range(0,2):
    if type(mainlist[k])==dict:
        print(mainlist[k].keys())
        print(mainlist[k].values())
    
 
#for k in mainlist:
 #   if type(k)==dict:
  #      print(k.keys())
   #     print(k.values())



    
