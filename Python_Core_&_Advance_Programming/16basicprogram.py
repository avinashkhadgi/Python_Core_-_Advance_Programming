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



    
    

    
def add():
    res = num1 + num2
    print("Result :-",res)
def subtract():
    res = num1 - num2
    print("Result :-",res)
def mul():
    res = num1 * num2
    print("Result :-",res)
def div():
    res = num1 / num2
    print("Result :-",res)

print("1. add")
print("2. subtract")
print("3. mul")
print("4. div")
choice = int(input("Enter your choice:-"))
if (choice>=1 and choice<=4):
    print("Enter two numbers:-")
    num1 = int(input("Enter first No:-"))
    num2 = int(input("Enter second No:-"))
    if choice == 1:
        add()
    if choice == 2:
        subtract()    
    if choice == 3:
        mul()
    if choice == 4:
        div()    
        
        










def add():
    res = num1 + num2
    print("Result :-",res)
def subtract():
    res = num1 - num2
    print("Result :-",res)
def mul():
    res = num1 * num2
    print("Result :-",res)
def div():
    res = num1 / num2
    print("Result :-",res)

print("1. add")
print("2. subtract")
print("3. mul")
print("4. div")
while True:
    choice = int(input("Enter your choice:-"))
    if (choice>=1 and choice<=4):
        print("Enter two numbers:-")
        num1 = int(input("Enter first No:-"))
        num2 = int(input("Enter second No:-"))
    if choice == 1:
        add()
    if choice == 2:
        subtract()    
    if choice == 3:
        mul()
    if choice == 4:
        div()    
        
