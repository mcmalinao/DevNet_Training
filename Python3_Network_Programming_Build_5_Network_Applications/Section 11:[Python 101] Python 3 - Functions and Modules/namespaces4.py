
def my_var_func():
    print(my_var)
    my_var = 10


# local definition
my_var_func()


##error:UnboundLocalError: local variable 'my_var' referenced before assignment
