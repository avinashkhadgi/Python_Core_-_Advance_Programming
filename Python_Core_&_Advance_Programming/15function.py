# def meaning ---> To define a function.

print("PCE")
def admission():  # called function...
    print("admission is open apply through CAP round")

admission() # calling function    
                      



def login():
    username = input("Enter your username:-")
    password = input("Enter your password:-")
    if username == password:
        print("Login successfully")
    else:
        print("You have enterd wrong credentails")    

login()  # calling fumction      
#admission()




def login():
    username = input("Enter your username:-")
    password = input("Enter your password:-")
    if username == password:
        print("Login successfully")
    else:
        print("You have enterd wrong credentails")    

login()  # calling fumction      





# simpe interest
def simple_interest():
    p = int(input("The priciple is:-"))
    t = int(input("The time period is:-"))
    r = int(input("The rate of interest is:-"))
    si = (p * t * r)/100
    print("Simple interest is",si)
    

simple_interest()
login()
admission()


#function defination

import time
def message():
    print("Vipul has comebaack")
message()    
print("first calling complete")
time.sleep(6)
message()
print("second time calling")
message()


#passing arguments
def online(name,msg):#called function
    print("welcome",name,"language",msg)

online("pythone","programming") #calling function
online("djngo","framwork")   #calling function


def addition(name):
    print("Addition of two no=",name+name)

addition(5)
addition(10)



def mul(name):
    print("mul of two no=",name*name)

mul(5)
mul(10)



#positional argument passing in correct order
def multi(a,b):
    return a*b
result=multi(10,20)    
print("multiplication result :-",result)


def add(a,b):
    return a+b
#result=add(10,20)    
print(add(10,20))




def chk_even_odd(number):
    if number%2==0:
        print(number,"This is even number")
    else:
        print(number,"This is odd number")
chk_even_odd(5)
chk_even_odd(10)        



# keyword argumnent
# we can pass argument values by keyword i.e by parameter name.
# here order is not matter but argument should be matched.

def func(fname,lname):
    print("HI",fname,lname)
func(fname="avinash",lname="khadgi")    


def func(fname,lname):
    print("HI",fname,lname)
func(lname="avinash",fname="khadgi")    





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# types of argument
# 1) Default argument
# 2) positional
# 3) keyword
# 4) variable length


# default argument

def func(city="nagpur"):
    print("I am from " + city)
func("delhi")
func("pune")
func()    



# unknown argument
def func(**name):
    print("my name is " + name["fname"])

func(fname = "avinash", lname = "khadgi")






 # returning multiple value at a time
def add_product(a,b):
     add=a+b 
     product=a*b
     return add,product
x,y=add_product(100,50)
print("The add is :- ",x)
print("The product is :- ",y)     



def func(name): # called function
    for i in name:
        print(i)
name_of_p = ["avinash","shraddha","vipul","ankush"]
func(name_of_p) # calling function




def func(name): # called function
    for i in name:
        print(i)
p ="avinash"
func(p) # calling function
