for i in range(5):
    try:
        print(i / 1)
    except   ZeroDivisionError:
        print("Division by 0 is just wrong!")
    print("The rest of the code....")

#output
#0.0
#The rest of the code....
#1.0
#The rest of the code....
#2.0
#The rest of the code....
#3.0
#The rest of the code....
#4.0
#The rest of the code...
