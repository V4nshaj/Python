class first:
    def first(self):
        a=eval(input("Enter A value"))
        b=eval(input("Enter B value"))
        c=a+b
        return c
class second(first):
    def read(self,c,d):
        n=obj.first()
        # print(type(n))
        e=n-c-d
        return e
obj=second()
print(obj.first())
print(obj.read(20,10))
