# Palindrome No or Not


x=int(input("Enter the no:-"))
if(str(x)[::-1]==str(x)):
    print("True")
else:
    print("False")    


 
 # Armstrong no or not

num=int(input("Enter the no:-"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
    
if(num==sum):
    print(num,"Is an Armstrong no")  
else:
    print(num,"Is an  Not Armstrong no")     
 


# WAP leap year or not....
#leap
# century--> Divvisible by 400.........////2000,1900
# Non century--> Divisible by 4......./////1978,,1998





year=int(input("Enter year:-"))
if year % 100 == 0:
    if year % 400 == 0:
        print("Enterd year is leap year")
    else:
        print("Enterd yera is not leap year")
else:
    if year % 4 == 0:
        print("Enterd year is leap year")
    else:
         print("Enterd year is not leap year")               



# WAP leap year or not 
year=int(input("Enter year:-"))
if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print("Enterd year is leap year")
else:
    print("Enterd year is not leap year")    


 


# Find out the biggest no among the three input numbers
n1=int(input("Enter the first no:-"))
n2=int(input("Enter the second no:-"))
n3=int(input("Enter the third no:-"))
if n1 > n2 and n1 > n3:
    print("Biggest no is :-",n1)
elif n2 > n3:
    print("Biggest no is :-",n2)
else:
    print("Biggest no is :-",n3)        
    


    

# factorial
 
num=int(input("Enter the no:-")) 
i=1
fact=1
while(i<=num):
    fact=fact*i
    i=i+1
print("Factorial of",num,"is",fact)    





# salary 

salary=float(input("Enter the salary:-"))
if (salary>=10000):
    salary=salary+salary*0.1
elif(salary>=6000 and salary<10000):
    salary=salary+salary*0.08
elif(salary<6000):
    salary=salary+salary*0.05
salary=round(salary,2)

print(salary)





# check even no.

list1 = [10,21,4,45,55,66,93]
for i in list1:
    if i % 2 == 0:
        print(i)



# check odd no.
list1 = [10,21,4,45,55,66,93]
for i in list1:
    if i % 2 != 0:
        print(i)
  

 # check positive no in a list..   
list1 = [-10,21,4,45,55,-66,-93]
for i in list1:
    if i >= 0:
        print(i)
  



 # check positive no in a list..  
 # by using  end== " " keyword o/p will be converted into vertical to horizontal line.
 
list1 = [-10,21,4,45,55,-66,-93]
for i in list1:
    if i >= 0:
        print(i,end=" ")
       
total = 0    
list1 = [10,21,4,45,55,66,93]
for i in range(0,len(list1)):
    total = total + list1
    print(total)



def simple_interest():
    p = int(input("The priciple is:-"))
    t = int(input("The time period is:-"))
    r = int(input("The rate of interest is:-"))
    si = (p * t * r)/100
    print("Simple interest is",si)
    

simple_interest()







from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))




import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))


ss=("python progtramming")
print(ss[5])



numm=int(input("Enter no:-"))
if numm % 2 ==0:
    print("Even")
else:
    print("odd")    
    
    

X = int(input("Enter no:-"))
if str(X)[::-1] == str(X):
    print("True")
else:
    print("False")       
    

num = int(input("Enter the no:-"))
sum = 0
temp= num
while temp > 0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print("Armstrong")
else:
    print("Not Armstrong")
       



num = int(input("Enter the no:-"))        
i=1
fact=1
while (i<=num):
    fact=fact*i
    i=i+1
print("Factorial of", num, "is", fact)    
    
        



year = int(input("Enter the year:-"))  
if year % 100 ==0 or year % 400 ==0 and year % 100 !=0 or year % 4==0:
    print("Leap")
else:
    print("Not Leap")    
    
    
    
ch=str(input("Enter any character:-"))
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
    print("Vowel")
else:
    print("consonent")        