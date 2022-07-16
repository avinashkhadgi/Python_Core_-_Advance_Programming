
rollno = [3,5,7,1,11,4,5,2,6]
for x in rollno:
    if x == 2 or x == 4 or x == 6 or x == 8 or x == 10:
        print("which even no is found",x)
        #break



mylist = [10,20,200,300,400,800,900,40,50]    
for i in mylist:
    if i > 300 :
        continue
    print(i)   


for i in range(10):
    if i%2==0:    # 0==0,1==0
        continue   
    print(i)






mylist = [10,20,200,300,400,800,900,40,50]    
for iteam in mylist:
    if iteam > 300 :
        print("this is not in my budget")
        continue
    print(iteam)   
else:
    print("you have purched everything")





ch=str(input("Enter any one character:-"))
if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" :
    print("This is Vowel")
else:
    print("Consonent")    



#error
'''
for ch in "avinash":
    print(ch)
if ch == "i" or ch == "s":
    break
print("current letter :",ch)
'''



#print("Hello {} {}! You just delved into python.".format(input(),input()))

#print("hhh")



p1=int(input("Enter percentage:-"))
if p1 < 100 and p1 >= 80:
    print("Your grade is A")
elif p1 <= 80 and p1 >= 60:
    print("Your grade is B")
elif p1 <= 60 and p1 >= 40:
    print("Your grade is C")
else:
    print("Sorryyy!!! You are Fail")             



s1=int(input("Enter papers marks:-"))
s2=int(input("Enter papers marks:-"))
s3=int(input("Enter papers marks:-"))
s4=int(input("Enter papers marks:-"))
s5=int(input("Enter papers marks:-"))
total=s1+s2+s3+s4+s5
print("total= ",total)
per=total//5
print("percentage = ",per)

if per < 100 and per >= 80:
    print("Your grade is A")
elif per <= 80 and per >= 60:
    print("Your grade is B")
elif per <= 60 and per >= 40:
    print("Your grade is C")
else:
    print("Sorryyy!!! You are Fail")             






a = "python is object oriented programming language"
print(a.find("python"))
print(a.find("object"))
print(a.find("language"))
print(a.find("javaa"))





a = ("avinash","shraddha","vipul","ankush")
s = '|' .join(a)
print(s)



a = "python is object oriented programming language"
print(a.lower())
print(a.upper())
print(a.swapcase())
print(a.title())
print(a.capitalize())




name = "avinash"
job = "Programmer"
age = 24
print("{} job is {} age is {}".format(name,job,age))
print("{0} job is {1} age is {2}".format(name,job,age))
print("{x} job is {y} age is {z}".format(x=name,y=job,z=age))




'''
print(input("name"))
print(input("sss"))
'''




# Hakerrank problem:----
print("Hello {} {}! You just delved into python.".format(input(),input()))

#print("hhh")



a = input("Enter your first name: ")
b = input("Enter your last name: ") 
#print("Hello ", a, b, "! You just delved into python.")

print("Hello  {} {} ! You just delved into python.".format(a,b))
