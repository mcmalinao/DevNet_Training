
import threading
import time

##Defining the main function
def myfunction():
    "Function to be executed"
    print("Start a thread")
    time.sleep(3)
    print("End a thread")

## run my function 5x concurrently  program to wait all threads to terminates

#Define an empty list of threads
threads = []

#Runs 5 concurrent sessions of myfucntion()
for i in range(5):
    th = threading.Thread(target = myfunction)
    th.start()      #starting the thread
    threads.append(th)
#Waiting for all threads to terminate
for th in threads:
    th.join()


###output  the start shows at the same time and 3 seconds after the end shows at the same time.

#Start a thread
#Start a thread
#Start a thread
#Start a thread
#Start a thread
#End a thread
#End a thread
#End a thread#
#End a thread
#End a thread
