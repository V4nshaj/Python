# function overloading
class PrintDT:
    def python_data(self, x=None):
        if isinstance(x, list):
            return x
        elif isinstance(x, tuple):
            return x
        elif isinstance(x, str):
            return x
        else:
            return 0


obj = PrintDT()
a1=obj.python_data(['banana', 'apple', 10])
l=len(a1)
print("List: ", a1)
a2=obj.python_data(('banana', 8, 'mango'))
print("Tuple: ", a2)
a3=obj.python_data("hello")
print("String: ", a3)
