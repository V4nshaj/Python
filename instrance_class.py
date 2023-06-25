class My_class:
    @classmethod
    def class_method(cls):
        return "This is a class method."
obj = My_class()
print(obj.class_method())
print(My_class.class_method())
# print(My_class.instance_method())-> instace cant be created due to @classmethod
My_class.instance_method(obj)