# Types of inheritance    
# 1) Single inheritance
# 2) Multilevel inheritance
# 3) Multiple inheritance

# 1) Single inheritance....

class Faculty: # parent class(derive class)
    def __init__(self,f_name,department,f_id):
        self.f_name = f_name
        self.department = department
        self.f_id = f_id

    def print_info(self):
        print("faculty information=",self.f_name,self.department,self.f_id)  


#obj = Faculty("avinash","ETC",1001)
#obj.print_info()      


class Cse(Faculty): # child class (base class)
    pass # no statments
obj = Cse("Shraddha","CSE",1002)
obj.print_info()


class Avi(Faculty):
    pass
obj = Avi("vipul","IT","1003")
obj.print_info()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 2) Multilevel inheritance..

class Collge: # fisrt clss first level
    def college_name(self):
        print("modern college")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Student(Collge):  # Second class second level
    def student_info(self):
        print("Name:- avinash khadgi")
        print("Branch :- ETC")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

class Exam(Student): # child class
    def subject(self):
        print("subject 1:- Python")
        print("subject 2:- Django")
        print("subject 3:- ML")

obj = Exam()
obj.college_name()
obj.student_info()
obj.subject()        




class Reg_login:
    def __init__(self): #constructor
        print("My name is constructor and i always excuted first")

    
    def reg(self): 
        self.n = input("name:-")
        self.id = input("id:-")
        self.pas = input("password:-")
        f = open("ookkt.txt","a")
        f.write(self.n+"-"+self.id+"-"+self.pas+"\n")
        f.close()
        print("Regestrationb successfuly")  
    
    def login(self):
        self.id1 = input("id:--")
        self.pas1 = input("password:--")
        if (self.id1 == self.id) and (self.pas1 == self.pas):
            print(" login successs")
        else:
            print("plese enter correct is and password")
    def show(self):
        print(self.n)
        print(self.id)                    

obj = Reg_login()
obj.reg()
obj.login()
obj.show()









class Reg: # fisrt class
    def __init__(self): #constructor
        print("My name is constructor and i always excuted first")
    def reg(self):
        self.n = input("name:-")
        self.id = input("id:-")
        self.pas = input("password:-")
        f = open("ookkt.txt","a")
        f.write(self.n+"-"+self.id+"-"+self.pas+"\n")
        f.close()
        print("Regestrationb successfuly")  
        #print(self.n)
class Login(Reg):  # second class 
    def __init__(self):
        print("My name is constructor and i always excuted first") 

    def login(self):      
        self.id1 = input("id:--")
        self.pas1 = input("password:--")
        if (self.id1 == self.id) and (self.pas1 == self.pas):
            print(" login successs")
        else:
            print("plese enter correct is and password")
            print(self.n)
    def show(self):
        print(self.n)
        print(self.id)
        
        
obj = Login()
obj.reg()
obj.login()
obj.show()        




class employee1():
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee(employee1):
    def __init__(self, name, age, salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
emp1 = employee1('harshit',22,1000)
 
print(emp1.age) 



# single inheritance


# Parent class
class ParentClass:
    def par_func(self):
         print("I am parent class function")

# Child class
class ChildClass(ParentClass):
    def child_func(self):
         print("I am child class function")

# Driver code
obj1 = ChildClass()
obj1.par_func()
obj1.child_func()

#`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Multi-level Inheritance:

# Parent class
class A:
   def __init__(self, a_name):
       self.a_name = a_name
   
# Intermediate class
class B(A):
   def __init__(self, b_name, a_name):
       self.b_name = b_name
       # invoke constructor of class A
       A.__init__(self, a_name)

# Child class
class C(B):
   def __init__(self,c_name, b_name, a_name):
       self.c_name = c_name
       # invoke constructor of class B
       B.__init__(self, b_name, a_name)
       
   def display_names(self):
       print("A name : ", self.a_name)
       print("B name : ", self.b_name)
       print("C name : ", self.c_name)

#  Driver code
obj1 = C('child', 'intermediate', 'parent')
print(obj1.a_name)
obj1.display_names()


#Multiple Inheritance:

# Parent class1
class Parent1:
   def parent1_func(self):
       print("Hi I am first Parent")

# Parent class2
class Parent2:
   def parent2_func(self):
       print("Hi I am second Parent")

# Child class
class Child(Parent1, Parent2):
   def child_func(self):
       self.parent1_func()
       self.parent2_func()

# Driver's code
obj1 = Child()
obj1.child_func()