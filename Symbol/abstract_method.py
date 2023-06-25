class Animal():
    def __init__(self, name):
        self.name=name
    
    def speak(self):
        #abstract method
        raise NotImplementedError("Subclass must implement this abstract method")
'''abstract method as the class Animal wants to overide the
speak method'''
class Dog(Animal):#inheritence
    def speak(self):
        return self.name+' says woof!'
class Cat(Animal):#inheritence
    def speak(self):
        return self.name+' says meow!'

fido=Dog("Fido")
kity=Cat('Kitty')
print(fido.speak())
print(kity.speak())