# Polymorphism example   

class Principle:
    def role(self):
        print("I am managing all activity of college")

class Dean:
    def role(self):
        print("Dean = I am decesion taking person")

class Hod:
    def role(self):
        print("Hod = i have responsibility of Teachers and students")

class Faculty:
    def role(self):
        print("faculty = I have to complete syallbus successfully")
#~~~~~~~~~~~~~~~ class declaration completed~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def func(obj):  # called func obj
    obj.role()  # calling func

campus=[Principle(),Dean(),Hod(),Faculty()]
for obj in campus:  # obj =1 principle =0
    func(obj)  # calling func  


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# how polymorphism implemented here
#==>>> ""Overloading"" in python
# 1) Operator overloading
# 2) Method overloading
# 3) Constractor overloading

#==>>> """Overriding""" in python
# 1) Method overriding
# 2) Constructor overriding

print("avinash"+"khadgi")
print(2+2)
print(2.5+2.5)  
#print("avinash"*4)

# 1)===>>> operator overloading
# operator overloading internally implemented by using magic method...


class Deposit:
    def __init__(self,cash):
        self.cash = cash

d1 = Deposit(1000)
d2 = Deposit(2000)
print(d1+d2)        


# Magic method avilable for every operator to overload any operator we have to override that method.
# the __add__method is a magic method which gets called when we add two numbers using the + operator.


class Deposit:
    def __init__(self,cash):
        self.cash = cash

    def __add__(self,other): # magic method........
        return self.cash + other.cash        

d1 = Deposit(1000)
d2 = Deposit(2000)
print("Total cash deposit amout=",d1+d2)        


# magic method avilabless....
'''
+ ==>> object.__add__(self,other)
- ==>> object.__sub__(self,other)
* ==>> object.__mul__(self,other)
/ ==>> object.__div__(self,other)
// ==>> object.__floordiv__(self,other)
% ==>> object.__mod__(self,other)
** ==>> object.__pow__(self,other)
+= ==>> object.__iadd__(self,other)
-= ==>> object.__isub__(self,other)
*= ==>> object.__imul__(self,other)
/= ==>> object.__idiv__(self,other)
//= ==>> object.__ifloordiv__(self,other)
%= ==>> object.__imod__(self,other)
**= ==>> object.__ipow__(self,other)
< ==>> object.__lt__(self,other)
<= ==>> object.__le__(self,other)
> ==>> object.__gt__(self,other)
>= ==>> object.__ge__(self,other)

'''
 

# 2)===>> Method overloading
 # in python Method overloading is """not possible"""
 # if we are trying to declare multiple method with same name add different no of arguments then python
 # will always consider only last method

class Arithmetic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)

obj = Arithmetic()
#obj.add(10)
#obj.add(10,20)
obj.add(10,20,30)                



# to handeld overloaded method in python
# if method with variable number of arguments required then we can handeld with defult arguments

class Arithmetic:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None:
            print(a+b)
        elif a!=None and b!=None and c!=None:
            print(a+b+c) 
        else:
            print("enter atlist two arguments")        

obj = Arithmetic()
obj.add(10)
obj.add(10,20)
obj.add(1,20,30)            



# 3)==>> Constructor overloading
# constructor overloading is not possible in python
# if we are define multiple constructor then the last constructor will be considere


class Arithmetic:
    def __init__(self):
        print("there is no argument")
    def __init__(self,a):
        print("passing one argumnet")
    def __init__(self,a,b):
        print("passing two argments")

obj = Arithmetic()
obj = Arithmetic(10)
obj = Arithmetic(5,5)                    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#======================================================================================================


#  

# 1) ==>> method overriding concepts

class Father:
    def bike(self):
        print("Bike")
    def laptop(self):
        print("Laptop with 2 GB RAM and 500 GB HDD")

class Child(Father):
    def laptop(self):
        print("As per my programming software requirment this is not cool for me")
        print("Laptop with 8 GB RAM and 1 TB HDD")

obj = Child()
obj.bike()
obj.laptop()                    


# 2) Constractor overriding 

class Father:
    def __init__(self):
        print("father:- i am on time at brekfast table")

class Child(Father):
    def __init__(self):
        print("child:- i am on time at brekfast table")

obj = Child()            





class Father:
    def __init__(self):
        print("father:- i am on time at brekfast table")

class Child(Father):
    def __init__(self):
        super().__init__() # using super() method we can  call parent class constructor
        print("child:- i am on time at brekfast table")

obj = Child() 
