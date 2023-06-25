class CTECH:
    pass #empty class pass statement is used that doesnt do anything 
class CINTEL:
    pass #empty class pass statement is used that doesnt do anything 
class NWC:
    pass #empty class pass statement is used that doesnt do anything 
class DSBS:
    pass #empty class pass statement is used that doesnt do anything 
company1 = CTECH()
company2 = CINTEL()
company3 = NWC()
company4 = DSBS()
print(isinstance(company1, CTECH))
print(isinstance(company2, CTECH))
print(isinstance(company3, CINTEL))
print(isinstance(company4, NWC))
print(isinstance(company3, NWC))
print(isinstance(company4, DSBS))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(CTECH, object))
print(issubclass(CINTEL, object)) 
print(issubclass(NWC, object)) 
print(issubclass(DSBS, object)) 
