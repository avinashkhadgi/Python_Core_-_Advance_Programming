# tuple represent  by () round or parenthesis  bracket......

mytuple=("avinash","vipul","ankush","shraddha","ruchika","shiwalee",22,"saurabh",30.97)
print(mytuple)
print(type(mytuple))

print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(mytuple[3])
print(mytuple[-1])
print(mytuple[2:5])
print(mytuple[:5])
print(mytuple[1:])
print(mytuple[:2])



'''mytuple[2]="rahul"
print(mytuple)'''


mytuple=("avinash","vipul","ankush","shraddha","ruchika","shiwalee",22,"saurabh",30.97)
print(mytuple)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# tuple is not changable................
'''
mytuple.append("disha")
print(mytuple)
'''

'''
mytuple.insert(3,"manish")
print(mytuple)
'''


'''
mytuple.remove("avinash")
print(mytuple)
'''
'''
newlist=mytuple.copy()
print(newlist)
'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mytuple=(("avinash","khadgi"),(33333,44444),(111002,22939))
print("Example of multidimensional list:-")
print(mytuple)
#print(mylist[row][col])
print(mytuple[0][0])
print(mytuple[0][1])
print(mytuple[1][0])
print(mytuple[2][0])
print(mytuple[2][1])




list1=("avinash","khadgi")
#print(list1*2)

print(type(list1))

list2=("shraddha","latkar")
list3=("vipul","margade")
print(list3+list1+list2)

'''
list1.clear()
print(list1)
'''




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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
#reverse() method
mylist=(50,40,30,20,10,5)
mylist.reverse()
print(mylist)
print(type(mylist))
'''