#useful when dealing with multiple files bcz here no need of closing of files
with open('text.txt', 'r') as file:
    contents = file.read()
    print(contents)