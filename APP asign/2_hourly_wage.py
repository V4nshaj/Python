import math

wage = float(input("Enter hourly wage for the worker: "))
hour = int(input('Enter the number of hours worked in past week = '))
if hour>40:
    tot = wage*40
    exhr = hour-40
    exwag = wage*150/100
    tot = tot + exwag*exhr
    print(f"Total wage for {hour} hours: ", tot)
else:
    tot = wage*hour
    print(f"Total wage for {hour} hours: ", tot)

