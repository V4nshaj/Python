#Introduction 
#-> represaents // single line comment
"""Triple quotes->Multi line comments same as/*
*/ """
"""print() is a predefined function in python use to print number, words, sentence,
float,character,etc or object
eg:
print("Hello World!")
print(6+3)
print(6-3)
print(6*3)
print(6/3)"""
"""For writing declaring a variable we can simply write
variable=1
variable="hello"
variable=42.54
variable='''Rohan and Harry 
are best friends'''->triple single quotes for multiline string
number=22
floatnum=22.7
deimal=.1111
"""
"""
we can change the data type of variable after declaration or initialization
eg:
number=22
#changing data type from int to string
a=str(num)
print(type(a))#here type function shows the data type of a in output screen:
<class 'string'>#for string conversion
<class 'int'>#for integer conversion
<class 'float'>#for float conversion
"""
#Implicit Conversion
x = 10
print("x is of type:",type(x))#print the data type of variable x shows integer
y = 10.6
print("y is of type:",type(y))
x = x + y
print(x)#printing the values
print("x is of type:",type(x))#print the data type of variable x shows float
#Explicit Conversion
# initializing string
s = "10010"
# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)
# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)
"""return f->"""
'''
find() vs rfind()
import string

def furl(str):
    start = str.find("http://")# find(“string”, beg, end)->find the position of the substring within a string.It takes 3 arguments, substring , starting index( by default 0) and ending index( by default string length). 
#It returns first occurrence of string if found.
    end = str.find(" ", start)#rfind(“string”, beg, end)->similar as find but returns the position of the last occurrence of string.
    return str[start:end] #string[start:end:step]

str = input("Enter url: ")
url = furl(str)
print("Url: ", url)'''