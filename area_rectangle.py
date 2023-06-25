class Rectangle:
    # constructor overloading based on args
    def __init__(self, *args):

        # if args are more than 1 multiple of args rectangle
        if len(args) > 1:
            self.res = 1
            for i in args:
                self.res *= i

        # if arg is an area of square the arg
        elif isinstance(args[0], int):
            self.res = args[0] * args[0]

a1 = Rectangle(4,5)
print("Area of Rectangle: ", a1.res)

a2 = Rectangle(2)
print("Area of square: ", a2.res)

'''
    l=0
    b=0
    def __init__(self):
        self.l = 0
        self.b = 0

    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    # def __init__(self, size):
    #     self.l = size
    #     self.b = size
    
    def display(self):
        print("Area = ", self.res)
    
    def area(self):
        self.res=self.l*self.b

obj = Rectangle(4,5)
obj.area()
obj.display()
# obj = Rectangle(2)
# obj.area()
# obj.display()'''