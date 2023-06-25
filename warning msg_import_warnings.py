import warnings
  
n = float(input("Enter a number:"))
  # displaying the warning message 
print(n)
if n!=int(n):
    warnings.warn('Warning Message: Not Integer')
else:
    warnings.warn(f'Warning Message: The value {n} is integer') 
