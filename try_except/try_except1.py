n = int(input('Enter numerator'))
d = int(input('Enter denominator'))
result = 0
try:
    result = n/d
    print(result)
except ZeroDivisionError:#zerodivisionerror is a built in exception
    print('Cannot divide by zero')
print(result)