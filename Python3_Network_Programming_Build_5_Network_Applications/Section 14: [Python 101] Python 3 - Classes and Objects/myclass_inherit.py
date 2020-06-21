## use when defining the class...
class MyNewRouter(MyRouter):
    "this is the class that descripts the charactericstics of a router."
    def __init__(self, routername, model, serialno, ios, portsno):
        MyRouter.__init__(self, routername, model, serialno, ios)
        self.portsno = portsno

    def print_new_router(self, string):
        print(string + self.model)
