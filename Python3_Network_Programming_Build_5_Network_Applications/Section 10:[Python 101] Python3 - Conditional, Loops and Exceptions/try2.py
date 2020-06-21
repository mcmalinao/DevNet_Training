for i in range(5):
    try:
        print(i / 0)
    except   NameError:
        print("You have a name error in your code!")


## python is not showing th line of code
#output
#Traceback (most recent call last):
#  File "try2.py", line 3, in <module>
#    print(i / 0)
#ZeroDivisionError: division by zero
