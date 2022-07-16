
#a user will have to enter until enterring avinash
name=""
while name!="avinash":
    name=input("Enter your name:-")
print("Thanks for entering valid name")    



# (in) is membership operator.....there is two membership operator[ in , not in]...............
print("List Iteration")
li=["avinash","vipul","shraddha","ankush"]
for i in li:
    print(i)


print("tuple Iteration")
li=("avinash","vipul","shraddha","ankush")
for i in li:
    print(i)
print(type(li))    





print("set Iteration")
li={"avinash","vipul","shraddha","ankush"}
for i in li:
    print(i)
print(type(li))    


print("string slicing")
a="avinash"
for i in a:
    print(i)



# for(ini;cond;inc/dec)
#{ 
    #//statement
# }


r=range(10)  #n=10,n-1=9
print(r)
for i in r:
    print(i)  # i = 0<10,1<10,2<10,,,,,9<10



r=range(15,30)
print(r)
for i in r:
    print(i)  # i=15,16,17,29<30


r=range(40,30,-1)
print(r)
for i in r:
    print(i)



l=list(range(15))
print(l)    





#WAP for change calculation with respect to total amount


Amount=int(input("please enter Amount for withdraw:-"))
print("100 notes =",Amount//100)
print("50 notes =",Amount//50)
print("20 notes =",Amount//20)
print("10 notes =",Amount//10)
print("5 notes =",Amount//5)




# WAP  to check weekend 

day=input("Enter day:-")
if day == "saturday" or day == "SATURDAY" or day == "sunday" or day == "SUNDAY":
    print("weekend")
elif day == "monday" or day == "tuesday" or day == "wednesday" or day == "thrusday" or day == "friday":
    print("working day")
else:    
    print("sorry!!Enter correct day")    
    
 
 
 



a = eval("10+20+30")
print(a)
b = eval("10*20*30")
print(b)



a = eval(("1280%100%50%20%10//5"))
print(a)




a = "avinash"
for i in a :
    if i == "v":
        print(i)


a = "avinash"
print(a[2])
print(a[-4])




li=[10,20,30,44,55,58]
sum=0
for i in li:
    sum=sum+i;
    print("Sum is",sum)

    

# factorial
 
num=int(input("Enter the no:-")) 
i=1
fact=1
while(i<=num):
    fact=fact*i
    i=i+1
print("Factorial of",num,"is",fact)



salary=float(input("Enter the salary:-"))
if (salary>=10000):
    salary=salary+salary*0.1
elif(salary>=6000 and salary<10000):
    salary=salary+salary*0.08
elif(salary<6000):
    salary=salary+salary*0.05
salary=round(salary,2)

print(salary)



   