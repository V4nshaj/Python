file = open('text', 'w')#creates a new text or rewrites the existing text on existing files
s = file.write('new content')
print(s)
file.close()

file1 = open('text.txt', 'a')#aappend modes adds
s = file1.write('new content')
file1.close()

file1 = open('text.txt', 'a')
content = '\nThis a new line'
file1.write(content)
file1.close()