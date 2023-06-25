import math

bp = float(input("Enter price of book: "))
q = int(input('Enter the Number of Copies = '))
dis = float(bp * 40 /100)
bp= float(bp - dis)
if q > 1:
    ship = ((q-1)*0.75)
    tot = float(bp*q + 3 + ship)
    print(f'Wholesale cost of {q} is  = $' , tot)

else:
    tot = float(bp + 3)
    print(f'Wholesale cost of {q} is  = $' , tot)