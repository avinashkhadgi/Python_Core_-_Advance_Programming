
class Student:
    roll_no = 101 # datamember it represent properties 

    def Student_info(self): # member function
        print("avinash")
        print("khadgi")
        print("1234566")

obj = Student()
print(obj.roll_no)
obj.Student_info()



class Employee:
    # class attribute
    company = "copyassignment.com"
    # constructor
    def __init__(self, name, age, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.salary = salary

# creating objects
emp1 = Employee("John", 34, 50000)
emp2 = Employee("Harry", 30, 60000)

# accessing class attributes using __class__ method
# syntax is-- instance.__class__.attribute
print(f"{emp1.name} and {emp2.name} work for {emp1.__class__.company}")

# accessing instance attributes
# syntax is-- instance.instance_attribute
print(f"{emp1.name}'s age is {emp1.age} and salary is {emp1.salary}")
print(f"{emp2.name}'s age is {emp2.age} and salary is {emp2.salary}")





#constructtor

class Newclass:
    def __init__(self): #constructor
        print("My name is constructor and i always excuted first")


    def show(self): # member function inside the class
        print("Welcome to class level programming")  

    def info(self):
        print("this is manually , using object we have to call")    

obj = Newclass()
obj.show()
obj.info()



class Hod:
    def __init__(self,name,age,empid):
        self.name=name
        self.age=age
        self.empid=empid

    def info(self):
        print("My name is :-",self.name)
        print("My age is :-",self.age)
        print("My emp id :-",self.empid)


obj = Hod("avinash","24","1001")
obj.info()






class Hod:
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no

    def show(self):
        print("My name is :-",self.name)
        print("My age is :-",self.age)
        print("My roll no :-",self.roll_no)



obj = Hod("avinash","24","1001")
obj.show()



# declering instance variable inside a constructor by using self varibale.
class Student:
    def __init__(self):
        self.s_name = "avi"
        self.f_name = "avi" # instance variable
        self.s_rollno = 101
        self.s_branch = "ETC"
        self.s_mb = 1234567890

obj = Student()
print(obj.__dict__)










class Avi():
    def Regestration(self):
        name = input("Enter name:-")
        id = int(input("Enter id no :-"))
        password = int(input("Enter password:-"))
        print("\t Regestration done sucessfully")
            

    def login(self):
        id1 = int(input("Enter id no :-"))
        password1 = int(input("Enter password :-"))
        #if id == id1 and password == password1:
        print("\t You have suceesfully login")
        


obj = Avi()
obj.Regestration()
obj.login()        







def Regestration():
    name = input("Enter name:-")
    id = (input("Enter id no :-"))
    password = (input("Enter password:-"))
    f = open("rrrr.txt","a")
    f.write(name+"-"+id+"-"+password)
    #f.write(name+"\n")
    #f.write(id+"\n")
    #f.write(password+"\n")
    f.close
    print("\t Regestration done sucessfully")
            

def login():
    id1 = (input("Enter id no :-"))
    password1 = (input("Enter password :-"))
    f = open("rrrr.txt","r")
    d=f.readlines()
    #l=len(d)
    #if(l==0):
        
    #g=d.split('-')
    #if(g[0]==search)
    print(d)
    print(d[0])
    print(d[1])
    print(d[2])
    
    if ((print(d[1])== id1 and print(d[2]) == password1)):
        print("\t You have suceesfully login")
    f.close()    

Regestration()

login()










# 1) >>>>declering instance variable inside a constructor by using self varibale.
class Student:
    def __init__(self):
        self.s_name = "avi"
        self.f_name = "avi" # instance variable
        self.s_rollno = 101
        self.s_branch = "ETC"
        self.s_mb = 1234567890

obj = Student()
print(obj.__dict__)



#2) >>>declaring instance varible inside a instance method by using self varible....

class Student:
    def __init__(self):
        self.s_name = "avi"
        self.f_name = "avi" 
        self.s_rollno = 101
        self.s_branch = "ETC"

    def getdata(self):
        self.s_mb = 1234567890

obj = Student()
obj.getdata()# untill and unless we call the method it will not added to the object.....
print(obj.__dict__)





# 3)>>> declaring the instance variable otside a class by using object....


class Student:
    def __init__(self):
        self.s_name = "avi"
        self.f_name = "avi" 
        self.s_rollno = 101
        #self.s_branch = "ETC"

    def getdata(self):
        self.s_mb = 1234567890

obj = Student()
obj.getdata()# untill and unless we call the method it will not added to the object.....
obj.s_branch = "ETC"  # adding instance varibale by using objectttttt....
print(obj.__dict__)



# accessing and deleting instance variable from the classs


class Student:
    def __init__(self):
        self.s_name = "avi"
        self.s_rollno = 101
        #self.s_branch = "ETC"

    def getdata(self):
        self.s_mb = 1234567890

obj = Student()
obj.getdata()# untill and unless we call the method it will not added to the object.....
obj.s_branch = "ETC"
del obj.s_rollno
#print(obj.s_name)
print(obj.__dict__)





# instance variable-->> create a seprate(copy) memory for each and every object...
# static variable -->> one copy(memory) will be created and it is aceesable for every object of the classs



class College:
    collegename = "Modern college"  # static variable..

    def __init__(self):
        self.studentname = "avinash"  # instance variable..

principle = College()
teacher = College()
accountant = College()

print("principle= ",principle.collegename,"|" ,principle.studentname)
print("teacher= ",teacher.collegename,"|" ,teacher.studentname)
print("accountant= ",accountant.collegename,"|" ,accountant.studentname)


College.collegename = "HBD"

principle.studentname = "avinash khadgi"

print("principle= ",principle.collegename,"|" ,principle.studentname)
print("teacher= ",teacher.collegename,"|" ,teacher.studentname)
print("accountant= ",accountant.collegename,"|" ,accountant.studentname)



# in construtor by using clss name
# in instance method by using clsss name 
# inclass method using class name or cls variable..
# static method by using class name...
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# how do we aceese static variable...
# inside a  instance method using self or class name..
# in construtor by using self or clss name
# outside the class using object or classs name...

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# types of method
# 1) static method
# 2) instance method
# 3) class method
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1) instance method...ex..

class Student:
    def __init__(self,name,rollno,mob): 
        self.name= name # instance variable
        self.rollno= rollno
        self.mob= mob

    def display(self): # instance method
        print(self.name, " ",self.rollno," ",self.mob)   

stud = Student("avinash",1001,123456667)
stud.display()


# 2) static method..ex..
# by using the class name we can access static method

class Student:
    @staticmethod # decorator
    def get_personal_detail(firstname,lastname):
        print("your personal details =",firstname,lastname)

    @staticmethod
    def contact_detail(mob_no,rollno):
        print("your contact details =",mob_no,rollno)

Student.get_personal_detail("avinash","khadgi")
Student.contact_detail(8989898989,10001)                




# implementing inner class concept...
class BE_FIRST_YEAR:
    def __init__(self):
        self.college_name = "PCE"
        self.branch_name = "ETC"
        self.objsem = self.Firstsem()

    def display(self):
        print("College name =",self.college_name)
        print("branch name = ",self.branch_name)

    # inner Class

    class Firstsem:
        def __init__(self):
            self.sub1 = "C"
            self.sub2 = "C++"
            self.sub3 = "Python"
            self.sub4 = "Java"
            self.sub5 = "C#"

        def show(self):
            print("subject1 =",self.sub1)
            print("subject2 =",self.sub2)
            print("subject3 =",self.sub3)
            print("subject4 =",self.sub4)
            print("subject5 =",self.sub5) 


obj = BE_FIRST_YEAR()
obj.display()
objsem = obj.objsem
objsem.show()



# Garbage collector program

import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

