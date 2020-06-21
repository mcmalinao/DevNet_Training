my_var = 5

def my_var_func():
    global my_var
    print(my_var)
    my_var = 10


# importing global my_var into function
my_var_func()
