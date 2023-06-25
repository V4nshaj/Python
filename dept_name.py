class Dept:

    def dep(self, s=None):
        if s != None:
            return s
        else:
            return 'SCO'


obj = Dept()
a1 = obj.dep("Science")
print("Department name: ", a1)
a2 = obj.dep("Math")
print("Department name: ", a2)
a3 = obj.dep()
print("Department name: ", a3)
