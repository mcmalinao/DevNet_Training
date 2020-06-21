try:
    print (4 / 0)
except NameError:
    print("NameError!")
finally:
    print("I dont care , im getting printed either way!")

#output

#I dont care , im getting printed either way!
#Traceback (most recent call last):
#  File "try_finally2.py", line 2, in <module>
#    print (4 / 0)
#ZeroDivisionError: division by zero
