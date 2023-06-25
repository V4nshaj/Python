class Compute:
    def Compute(self, x=None, y=None):
        if x != None and y != None:
            return x*y
        elif x != None:
            return x*x
        else:
            return 0


obj = Compute()
x1 = obj.Compute()
print("Area = ", x1)
x2 = obj.Compute(6)
print("Area of square= ", x2)
x3 = obj.Compute(2, 8)
print("Area of rectangle = ", x3)
