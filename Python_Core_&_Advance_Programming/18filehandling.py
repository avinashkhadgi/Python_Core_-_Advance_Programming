
f = open("myfile.txt","w")
print("name of file",f.name)
print("file mode",f.mode)
print("readable",f.readable())
print("writeable",f.writable())
f.close()
print("file has closed",f.closed)




# performing write operation

f = open("covid.txt","w")
f.write("maintain social distancing")
print("written work has done succefully")
f.close()




#inserting list

f = open("covid.txt","w")
mylist = ["avinash","vipul","pranay"]
f.writelines(mylist)
print("written work has done succefully")
f.close()





#reading data from a file

f = open("covid.txt","r")
print(f.read())
print(f.read(1))
print(f.readline())
print(f.readlines())
f.close()




with open("myfile.txt","w") as f:
    f.write("avinash\n")
    f.write("vipul\n")
    print("file closed",f.closed)
print("file closed",f.closed)    



f = open("myfile.txt","r")
print("current index position of file pointer ",f.tell())
print(f.read(13))



# reading and writing binary data
f1 = open("avinash.jpeg","rb")
f2 = open("khadgi.jpeg","wb")
data = f1.read()
f2.write(data)
print("new image avilable with the name:-")
f1.close
f2.close






f1 = open("kajal.JPEG","rb")
f2 = open("vip.jpeg","wb")
data = f1.read()
f2.write(data)
print("new image avilable with the name:-")
f1.close
f2.close



# operation with csv file
import csv
f = open("student.csv","w",newline="")
a = csv.writer(f)
a.writerow(["rollno","name","mobno"])
rollno = 101
name = "avinash"
mob = 9579126469
a.writerow([rollno,name,mob])
print("student record has save")





# operation with csv file
import csv
f = open("aviii.csv","w",newline="")
a = csv.writer(f)
a.writerow(["rollno","name","mobno"])
rollno = 101
name = "avinash"
mob = 9579126469
a.writerow([rollno,name,mob])
print("student record has save")





import csv
f = open("student_new.csv","w",newline="")
a = csv.writer(f)
a.writerow(["name","rollno","emailid","address","mobnumber","p1","p2","p3","p4","p5","total","per","result"])
name = "avinash"
rollno = 105
emailid = "avinashkhadgi30@gmail.com"
address = "Jagnath Budhwari Nagpur"
mobno = 9579126469
p1 = int(input("Enter p1 marks:-"))
p2 = int(input("Enter p2 marks:-"))
p3 = int(input("Enter p3 marks:-"))
p4 = int(input("Enter p4 marks:-"))
p5 = int(input("Enter p5 marks:-"))
total = p1+p2+p3+p4+p5
per = total/5
if (p1 > 40 and p2 > 40 and p3 > 40 and p4 > 40 and p4 > 40):
    result = "pass"
else:
    result = "fail"  
a.writerow([name,rollno,emailid,address,mobno,p1,p2,p3,p4,p5,total,per,result])     
print("student record has save")

