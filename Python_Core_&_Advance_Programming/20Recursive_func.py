
def recursive_factorial(n):   
   if n == 1:   
       return n   
   else:   
       return n * recursive_factorial(n-1)   
print("Factorial of 5 is :-",recursive_factorial(5))  
print("Factorial of 4 is :-",recursive_factorial(4))
a = int(input("No :-"))
print("Factorial is :-",recursive_factorial(a))



def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
print("Factorial of 4 is :-",fact(4))    
a = int(input("No :-"))
print("Factorial is :-",fact(a))        





# *args and **kwargs in Python
# we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
#Special Symbols Used for passing arguments:-

#1.)*args (Non-Keyword Arguments)

#2.)**kwargs (Keyword Arguments)



# Python program to illustrate 
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print (arg)
   
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')



# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *argv):
    print ("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')



# Python program to illustrate 
# *kwargs for variable number of keyword arguments
 
def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks')  




# Python program to illustrate  **kwargs for
# variable number of keyword arguments with
# one extra argument.
 
def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')  




#Using *args and **kwargs in same line to call a function
#Example:

def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
 
# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")