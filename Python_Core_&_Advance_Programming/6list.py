#..list represented by    [] sqare bracket ........

mylist=["avinash","vipul","ankush","shraddha","ruchika","shiwalee",22,"saurabh",30.97]
print(mylist)
print(type(mylist))

print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[:2])



mylist[2]="rahul"
print(mylist)

mylist[3:6]="prashant","amit","roshan"
print(mylist)




mylist=["avinash","vipul","ankush","shraddha","ruchika","shiwalee",22,"saurabh",30.97]
print(mylist)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# .append() method used automatically add object in last position..
mylist.append("disha")
print(mylist)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  .insert() method performing the operation of shifted in right side
mylist.insert(3,"manish")
print(mylist)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# .remove() method remove any object
mylist.remove("manish")
print(mylist)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

newlist=mylist.copy()
print(newlist)


#print(mylist)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mylist=[["avinash","khadgi"],["30.97"],[111002,22939]]
print("Example of multidimensional list:-")
print(mylist)
#print(mylist[row][col])
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])

#instead of multidimension list dictionary will be better choice
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

list1=["avinash","khadgi"]
#print(list1*2)

print(type(list1))

list2=["shraddha","latkar"]
list3=["vipul","margade"]
print(list3+list1+list2)


list1.clear()
print(list1)






#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
name="avinash"
print(name)
myname=list(name)
print(myname)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#we have used list constructor

name="help4code containing 5000 plus programs"
print(name)
#mylist=list(name)
#print(name)
mylist=name.split()
print(mylist)
print(name)



#reverse() method
mylist=[50,40,30,20,10,5]
mylist.reverse()
print(mylist)








# sort asending desending

l1 = [10,3,22,89,90,27,11,34]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)



l1 = [1,1,2,2,3,3,4,4,4,5,6,6,7,7,7,7,9]
print(l1.count)
print(l1.count(1))
print(l1.count(7))

print(l1.count(11))