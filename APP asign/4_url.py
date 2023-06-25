import string

def furl(str):
    start = str.find("http://")
    end = str.find(" ", start)
    return str[start:end] #string[start:end:step]

str = input("Enter url: ")
url = furl(str)
print("Url: ", url)