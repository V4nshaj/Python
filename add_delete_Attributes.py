class SRMIST:
    school = 'Btech'
    dept1 = 'management' 
    dept2 = 'Science' 
    dept3 = 'Math' 
    dept4 = 'Python' 

print("Original attributes and their values of the SRMIST class:")
for attr, value in SRMIST.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
print("\nAfter adding the student_class, attributes and their values with the said class:")
SRMIST.dept5 = 'Java'
for attr, value in SRMIST.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
print("\nAfter removing the dept1, dept2 attributes and their values from the said class:")
del SRMIST.dept1
del SRMIST.dept2
#delattr(SRMIST, 'dept1', 'dept2')
for attr, value in SRMIST.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')