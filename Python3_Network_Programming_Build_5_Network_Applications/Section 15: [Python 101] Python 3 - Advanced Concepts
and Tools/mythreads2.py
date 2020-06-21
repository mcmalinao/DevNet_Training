
import threading
import time

def myfunction():
    print("Start a thread")
    time.sleep(3)
    print("End a thread")

## run my function 5x concurrently  program to wait all threads to terminates
## this time removing threading related code..
threads = []

for i in range(5):
    myfunction()

#    th = threading.Thread(target = myfunction)
#    th.start()
#    threads.append(th)

#for th in threads:
#    th.join()


###output

#Start a thread
#End a thread
#Start a thread
#End a thread
#Start a thread
#End a thread
#Start a thread
#End a thread
#Start a thread
#End a thread
