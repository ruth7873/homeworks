from MyClass import MyClass


class MySubclass(MyClass):

    def __init__(self, var1, var2, var3):
        super().__init__(var1, var2, var3)

    def set_private_var(self, value):
        print("Overriding set_private_var method")
        super().set_private_var(value)

    def static_function(self):
        print("Overriding static_function method")