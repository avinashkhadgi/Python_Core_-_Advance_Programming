#   set rrepresent by {} curly bracket......

myset={1,2,3,4,5,'avinash',30.97,'vipul','shraddha','ruchika',22.97,'shiwalee'}
print(myset)
print(type(myset))

#print(myset[0])
#set is growable in nature ,based on our requirement we can increase or decrease the size.....

myset.add(70)
print(myset)
#if we want to add more than one item then we should go for update()
#update() method can take multiple argument but all must be iterable 




fs=frozenset(myset)
print(type(fs))
print(fs)

myset.update(range (22,30))
print(myset)



#myset.append("disha")
#print(myset)



#union() method add yourset{} item into myset{}
myset={10,20,30,40,50}
yourset={"avinash","khadgi"}
newset=myset.union(yourset)
print(newset)





#insertion return common element

myset={10,20,30,40,50,60}
yourset={20,30,60,70,90}
print(myset.intersection(yourset))


#difference() method this will return the element present in myset but not in yourset
myset={10,20,30,40,50}
yourset={10,30,50,60}
print(myset.difference(yourset))


