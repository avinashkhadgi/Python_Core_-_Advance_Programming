
a = int(input("Enter first integer no :-"))
b = int(input("Enter second integer no :-"))
print(a/b)




a = int(input("Enter first integer no :-"))
b = int(input("Enter second integer no :-"))
try:
    print(a/b)
except:
    print("Please ensure that you can't divide any no by zero")    



try:
    print(2/0)

except ZeroDivisionError as message:  # division by zero
    print("The description of exception:",message)    


try:
    a = int(input("Enter first integer no:-"))
    b = int(input("Enter second integer no:-"))
#multiple except block
#try:
    print(a/b)
except ZeroDivisionError as message:
    print("Please ensure that you can't divide any no by zero:-",message)    
except ValueError as message:
    print("Enter only interger no:-",message)    




#handling multiple differenrt kinds of exception with single except block

try:
    a = int(input("Enter first Integer no:-"))
    b = int(input("Enter second Interger no:-"))
    print(a/b)
except (ValueError,ZeroDivisionError) as message:
    print("Emter correct no:-",message)   
 


# defalult except block
try:
    a = int(input("Enter first Integer no:-"))
    b = int(input("Enter second Interger no:-"))
    print(a/b)
except (ValueError,ZeroDivisionError) as message:
    print("Emter correct no:-",message)   
except:
    print("This is default part of except block")    



while True:

    try:
        a = int(input("Enter first Integer no:-"))
        b = int(input("Enter second Interger no:-"))
        print(a/b)

    except (ValueError,ZeroDivisionError) as message:
        print("Emter correct no:-",message)  
    except:
        print("This is default part of except block") 




# we can use else block if no error will generate it is depend on our own need and necessity
try:
    a = int(input("Enter first Integer no:-"))
    b = int(input("Enter second Interger no:-"))
    print(a/b)
except (ValueError,ZeroDivisionError) as message:
    print("Emter correct no:-",message)   
except:
    print("This is default part of except block")    
else:
    print("Everything is okey")    







# Finally block will always executed  whether try block generate error or not

try:
    a = int(input("Enter first Integer no:-"))
    b = int(input("Enter second Interger no:-"))
    print(a/b)
except (ValueError,ZeroDivisionError) as message:
    print("Emter correct no:-",message)   
except:
    print("This is default part of except block")    
finally:
    print("I will always executed")    
    





# nested try except block

try:
    a = int(input("Enter first integer no:-"))
    b = int(input("Enter second integer no:-"))

    try:
        print(a/b)
    except (ZeroDivisionError) as message:
        print("Please ensure that you can't divide any no by zero:-",message)    
except (ValueError) as message:
    print("Enter only interger no:-",message)  



# user defined exception by raise keyword:---

obj = 50
if obj > 40:
    raise Exception("Value 40 are not greter than 50....")




# python logging..
import logging
logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
logging.debug("This indicates debugging informtion")
logging.info("this indicates the important information")
logging.error("this indicates the error information")
logging.warning("this indicates the warning information")
logging.critical("this indicates the critical information")



import logging
logging.basicConfig(filename="exception.txt",level=logging.DEBUG)
try:
    a = int(input("Enter first Integer no:-"))
    b = int(input("Enter second Interger no:-"))
    print(a/b)
except (ValueError,ZeroDivisionError) as message:
    print("Emter correct no:-",message)   
    logging.exception(message)

   
import logging
logging.basicConfig(filename="exception2.txt",level=logging.DEBUG)
try:
    a = int(input("Enter first Integer no:-"))
    b = int(input("Enter second Interger no:-"))
    print(a/b)
except (ValueError,ZeroDivisionError) as message:
    print("Emter correct no:-",message)   
    logging.exception(message)

 






