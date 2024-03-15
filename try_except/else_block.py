n = int(input('Enter numerator'))
d = int(input('Enter denominator'))
try:
    result = n/d
except ZeroDivisionError:#zerodivisionerror is a built in exception
    print('Cannot divide by zero')
else:
    print(result)
