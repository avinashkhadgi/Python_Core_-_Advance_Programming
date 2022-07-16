
# main Thread program


import threading
print("current executive thread name:-",threading.current_thread().getName())
# here current_thread() return Thread object
# here getName() method return current executive thread name



# creating a thread without using any class

from threading import *
import time
def activate():
    for i in range(1,3):
        time.sleep(2)
        print("this is child thread")

t = Thread(target=activate) # creating thread object
t.start() # starting of thread
#~~~~~~~~~~~~~~~~~~~~~~~~~~ Child threas~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in range(1,3):
    time.sleep(2)
    print("This is main thread") # main thread



# when we call start () method then tread will create
# creating a thread by extendiing thread clss
# whenever we call start() method then automatically run() method will be executed ....

from threading import*
import time
class MyThread(Thread): # child class
    for i in range(3):
        time.sleep(2)
        print("child thread")

obj_t= MyThread()        
obj_t.start()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main thread section~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in range(3):
    time.sleep(2)
    print("main thread")






# creating a Thread without extending thread class:

from threading import*
class Mytest:
    def display(self):
        for i in range(4):
            print("child thread\n")
obj = Mytest()
t = Thread(target=obj.display)
t.start() 

for i in range(4):
    print("main thread")


# check with withouttttt multi threading

from threading import*
import time
def add(num): #[2,4,6,8,9]
    for n in num:
        time.sleep(1)
        print("Add:-",2+n)
        print()
def mul(num): # [2,4,6,8,9]
    for n in num:
        time.sleep(1)
        print("Mul:-",n*n)
        print()
def sub(num): # [2,4,6,8,9]
    for n in num:
        time.sleep(1)
        print("Sub:-",n-n)
        print()               
num = [2,4,6,8,9] # list name of num
starttime = time.time()
add(num) # calling func
mul(num) # calling func
sub(num) # calling func
print("The total time:-",time.time()-starttime)


 # With Multithreading we can see same programmm

from threading import*
import time
def add(num): #[2,4,6,8,9]
    for n in num:
        time.sleep(1)
        print("Add:-",2+n)
        print()
def mul(num): # [2,4,6,8,9]
    for n in num:
        time.sleep(1)
        print("Mul:-",n*n)
        print()
def sub(num): # [2,4,6,8,9]
    for n in num:
        time.sleep(1)
        print("Sub:-",n-n)
        print()               
num = [2,4,6,8,9] # list name of num
starttime = time.time()
t1 = Thread(target=add,args=(num,))
t2 = Thread(target=mul,args=(num,))
t3 = Thread(target=sub,args=(num,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("The total time:-",time.time()-starttime)



from threading import*
import time
def show():
    for i in range(3):
        print("mythread")
        time.sleep(2)

t=Thread(target=show)   
t.start()
t.join(2) # this line executed by main thread
for i in range(3): 
    print("your thread")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ident(thread identification number)
# every thread internally having UID numbers, and that can be get by implicit variable ident

from threading import*
def show():
    print("child thread")
child = Thread(target=show)
child.start()
print("main thread ID",current_thread().ident)
print("child thread ID",child.ident)    



# join() method...
# if we are executing  multiple thread and we want to  wait until completing some other thread
# then we have to use join() method..

from threading import*
import time
def show():
    for i in range(3):
        print("child thread")
        time.sleep(2)

child = Thread(target=show)
child.start()
child.join()

for i in range(3):
    time.sleep(1)
    print("main thread")

# we can pass time period in join() also join(seconds)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Deamon thread...

from threading import*
print(current_thread().isDaemon())     
'''
'''
from threading import*
print(current_thread().isDaemon())   
print(current_thread().setDaemon(True))  


from threading import*
import time
def show():
    print("child thread")
obj = Thread(target=show)
print(obj.isDaemon())
obj.setDaemon(True)
print(obj.isDaemon())




# Thread Synchronization
# synchronization means ===>>  co-ordination with same steps/tasks etc...
# without synchronization

from threading import*
import time
def conferenceCell(myname):
    print("HI i am =")
    time.sleep(1)
    print(myname)

obj = Thread(target=conferenceCell,args=("avinash",))
obj2 = Thread(target=conferenceCell,args=("khadgi",))
# here two object(obj,obj2) are going to access same method at same time
obj.start()
obj2.start()





from threading import*
import time
l = Lock()
def come_in(name):
    l.acquire()
    for i in range(4):
        print(name)
        print("Yes sir =",end='')
        time.sleep(1)

    l.release()
    

obj = Thread(target=come_in,args=("avinash",))
obj2 = Thread(target=come_in,args=("khadgi",))
# here two object(obj,obj2) are going to access same method at same time
obj.start()
obj2.start()





# problems in thread block
# if the lock already hold by one thread and at the same time some other thread acquire same
# then it will be blocked....[console screen block]


from threading import*
obj = Lock()
print("First time acquire the lock")
obj.acquire()
print("second time acquire the lock")
obj.acquire()


# Solution is RLock(Reenterent lock) the same thread can acquire the lock again and again

from threading import*
obj = RLock()
print("First time acquire the lock")
obj.acquire()
print("second time acquire the lock")
obj.acquire()



# synchronization with semaphore

from threading import*
import time
l = Semaphore(4)
def come_in(name):
    l.acquire()
    for i in range(4):
        print(name)
        print("Yes sir =",end='')
        time.sleep(1)

    l.release()
    

obj = Thread(target=come_in,args=("avinash",))
obj2 = Thread(target=come_in,args=("khadgi",))
obj3 = Thread(target=come_in,args=("shraddha",))
obj4 = Thread(target=come_in,args=("vipul",))
# here two object(obj,obj2) are going to access same method at same time
obj.start()
obj2.start()
obj3.start()
obj4.start()










