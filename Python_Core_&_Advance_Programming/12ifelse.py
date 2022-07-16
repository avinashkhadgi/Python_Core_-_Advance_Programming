#W.A.P eligible or not.
age=int(input("Enter your age:-"))
if age>18:
    print("You are eligible")
else:
    print("you are not eligible")
   



# 
name=input("Enter name:-")
if name=="avinash":
    print("hello my name is avinash but i am not a tester")
else:
    print("did not match the pattern")



# Enter the no is positive negetive or zero.
a=int(input("Enter any number:-"))

if a > 0:
    print("No is positive")
if a < 0:
    print("No is negative")
if a == 0:
    print("No is zero")        





#
brand =input("Enter your colddrink name:-")
#if brand=="pepsi" or "PEPSI":
#if brand== "pepsi" :
if brand=="pepsi" or brand=="PEPSI" :
    print("swag")
elif brand == "dew" or brand=="DEW":
    print("Dar ke age jeet hai")
elif brand == "thumbsup" or brand=="THUMBSUP" :
    print("Teste the thunder")    
else:
    print("go for other brand")    




# find the biggest no.
n1=int(input("Enter the first no:-"))
n2=int(input("Enter the second no:-"))
n3=int(input("Enter the third no:-"))
if n1 > n2 and n1 > n3:
    print("Biggest no is :-",n1)
elif n2 > n3:
    print("Biggest no is :-",n2)
else:
    print("Biggest no is :-",n3)        


# 
print("samsung , nokia , vivo , oppo ")
brand=input("Enter brand :-")
cost=int(input("enter cost:-"))
if brand=="samsung" and cost > 10000:
    print("J7,Note 7, Note 8 , Note 9")
elif brand== "nokia" and cost < 10000:
    print("Nokia2690, Nokia1100, Nokia150 ")    
elif brand=="vivo" and cost > 10000:
    print("vivo v7, vovo 8, vivo 9")
elif brand=="oppo" and cost > 15000:
    print("oppo A5 , oppo A6, oppo A7")    
else:
    print("Sorry !!!!!!plese enter correct brand and cost")







# Grade
p1=int(input("Enter percentage:-"))
if p1 < 100 and p1 >= 80:
    print("Your grade is A")
elif p1 <= 80 and p1 >= 60:
    print("Your grade is B")
elif p1 <= 60 and p1 >= 40:
    print("Your grade is C")
else:
    print("Sorryyy!!! You are Fail")             


# percentage with Grade.
s1=int(input("Enter papers marks:-"))
s2=int(input("Enter papers marks:-"))
s3=int(input("Enter papers marks:-"))
s4=int(input("Enter papers marks:-"))
s5=int(input("Enter papers marks:-"))
total=s1+s2+s3+s4+s5
print("total= ",total)
per=total//5
print("percentage = ",per)

if per < 100 and per >= 80:
    print("Your grade is A")
elif per <= 80 and per >= 60:
    print("Your grade is B")
elif per <= 60 and per >= 40:
    print("Your grade is C")
else:
    print("Sorryyy!!! You are Fail")             




# WAP leap year or not....
#leap
# century--> Divvisible by 400.........////2000,1900
# Non century--> Divisible by 4......./////1978,,1998





year=int(input("Enter year:-"))
if year % 100 == 0:
    if year % 400 == 0:
        print("Enterd year is leap year")
    else:
        print("Enterd yera is not leap year")
else:
    if year % 4 == 0:
        print("Enterd year is leap year")
    else:
         print("Enterd year is not leap year")               



# WAP leap year or not using operator.
year=int(input("Enter year:-"))
if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print("Enterd year is leap year")
else:
    print("Enterd year is not leap year")    



#
a=int(input("Enter value of a:-"))
b=int(input("Enter value of b:-"))
c=int(input("Enter value of c:-"))

if a > b:
    if a > c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b > c:
        print("b is greater")
    else:
        print("c is greater")                
     