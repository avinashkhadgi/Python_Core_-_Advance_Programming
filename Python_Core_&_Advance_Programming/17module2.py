# import means ---> If you want to access one file to another file then you should go for import

# first way
import module1   
module1.welcome("avinash","khadgi")
module1.square(4)


# second way
import module1 as mod 
mod.welcome("avinash","khadgi")



# third way 
from module1 import square,welcome
square(5)
welcome("avinash","khadgi")




# import* meaning-----> All accessable    everything
from module1 import*
username=str(input("enter username:-"))
password=str(input("enter password:-"))
login(username,password)
print(pi)
welcome("vipul","shraddha")

