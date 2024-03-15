file=open('text.txt', 'r')
print(file)
content1 = file.read()
print(content1)
content2 = file.read(5)#read upto 5 bytes of character
print(content2)
content3 = file.readline()#reaads first line
print(content3)
file.close()#if some file is accessess the content of the file the file will not able to access