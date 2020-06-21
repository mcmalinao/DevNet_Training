for i in range(5):
    try:
        print(i / 1)
    except ZeroDivisionError:
        print("Division by 0 is just wrong!")
    except NameError:
        print("Name error detected!")
    except ValueError:
        print("Won value!")


#best practices to have more except clasue..
