
mydict = {
    "100": "avinash",
    "101": "vipul",
    "102": "shraddha",
    "103": "ankush",
    "104": "khadgi",
}
print(mydict)



#with the help of key we have to print values
a=mydict["101"]
print(a)



#we will replace old value by new value

mydict["104"]="roshit"
print(mydict)



# pop() using remove any object
mydict={
    102:"avinash",
    "professional": "devloper",
    "empid": 3097
}

mydict.pop(102)
print(mydict)


mydict ["mobile no"] = 9579126469
mydict ["Department"] = "ETC"
mydict ["Department"] = "IT"
mydict ["change"] = "ETC"
print(mydict)



# copy()  method.......
mydict={
    "name":"avinash",
    "professional": "devloper",
    "empid": 3097
}

newdict=mydict.copy()
print(newdict)




# return string.........
x="Hello World"
print(x[::-1])




x="HelloWorld"
print(x[:])
print(x[1:])
print(x[:5])
print(x[5:])



a=[20,30,50]
b=[1,41,60]
print(a<b)


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
        
    
    