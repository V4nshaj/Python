import string


def right_justify(str, length):
    return ' '*(length - len(str)) + str


str = input("Enter string: ")
length = int(input("Enter the length of column: "))
a = right_justify(str, length)
print(f"The last letter of the string is in column {length} of the display: ")
print(a)
