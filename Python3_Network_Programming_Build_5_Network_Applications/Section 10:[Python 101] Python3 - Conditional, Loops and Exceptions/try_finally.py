try:
    print (4 / 2)
except NameError:
    print("NameError!")
finally:
    print("I dont care , im getting printed either way!")

#output
#2.0
#I dont care , im getting printed either way!
