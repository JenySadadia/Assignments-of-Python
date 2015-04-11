l1=[1,'a','$','jeny']
print "First list l1:-",l1

l2=[2,4,["a",34,"bvn"],'b']
print "Second list l2:-",l2

l1.append(3)
l3=l1
print "Append l1 with int 3 :-",l3

l1.extend(l2)
l4=l1
print "Extend l1 with l2:-",l4

l1.append(l2)
l5=l1
print "Append l1 with l2:-",l5
