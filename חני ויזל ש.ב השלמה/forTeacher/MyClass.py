

class MyClass:
    def __init__(self, var1=1, var2=2, var3=3):
        self._private_var = var1
        self._protected_var = var2
        self.public_var = var3

    def get_private_var(self):
        return self._private_var

    def set_private_var(self, value):
        self._private_var = value

    @property
    def protected_var(self):
        return self._protected_var

    @protected_var.setter
    def protected_var(self, value):
        self._protected_var = value

    @staticmethod
    def static_function():
        return "This is a static method"



