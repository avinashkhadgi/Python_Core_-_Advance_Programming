
import re
count = 0
pattern = re.compile("python")
matcher = pattern.finditer("A function in python is defined a def statment. python is best lan for beginner.python is a best programming lan.")
for i in matcher:
    count+=1
    print(i.start(),"---",i.end(),"---",i.group())
print("The no of occurances :-",count)    



import re
count = 0
#pattern = re.compile("python")
matcher = re.finditer("hi","avinash hi Hi avinash hi Hi hishraddha hi vipul")
for i in matcher:
    count+=1
    print(i.start(),"---",i.end(),"---",i.group())
print("The no of occurances :-",count)    






import re
obj = input("Enter any character:-")
objmatch = re.finditer(obj,"a7b @k9z")
for match in objmatch:
    print(match.start(),".....",match.group())




#  here are the cheching quntifier i.e the no of time match occure

import re
obj = input("Enter any character:-")
objmatch = re.finditer(obj,"hellohihowareyou")
for match in objmatch:
    print(match.start(),".....",match.group())



# match() fuction operation

import re
a = input("Enter string to perform match operation:-")
match = re.match(a,"python is very important")
if match!=None:
    print("match found at begining level")
    print(match.start()," ",match.end())
else:
    print("there is no matching at beginiing level")    



# fullmatch()

import re
a = input("Enter string to perform match operation:-")
match = re.fullmatch(a,"pythonisvery")
if match!=None:
    print("match found at begining level")
    print(match.start()," ",match.end())
else:
    print("there is no matching at beginiing level")    



# search () function

import re
a = input("Enter string to perform match operation:-")
match = re.search(a,"python is very important")
if match!=None:
    print(match.start()," ",match.end())
else:
    print("there is no matching at beginiing level")    


# findall () function

import re
match = re.findall("[0-9]","ab2c3dj9bgh5kff")
print(match)



# sub () function
# re.sub(expression,replacement,string)

import re 
obj = re.sub("[0-9]","#","ab3gd7hvbj1jg6v7")
print(obj)


# subn() function

import re 
obj = re.subn("[0-5]","@","ab3gdnk1j7k8")
print(obj)
print("the string is :-",obj[0])
print("the no of replacement is :-",obj[1])



# split() fumction

import re
obj = re.split(" - ","avinash vipul shraddha ruchika ankush")
print(obj)
#for o in obj:
 #   print(o)



# Wap to check valid mobile no

import re
mo = input("Enter mobile no:-")
obj = re.fullmatch("[0-9]\d{9}",mo)
print(obj)
if obj!=None:
    print("Valid mob no")
else:
    print("invalid mob no")  




# WAP to check a valid password

import re
ps = input("Enter  password:-")
obj = re.match("[a-zA-Z0-9]",ps)
print(obj)
if obj!=None:
    print("Valid password")
else:
    print("invalid password")  


          