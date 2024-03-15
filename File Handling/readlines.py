with open('text.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    lines = file.readlines()

print(line1)
print(line2)
print(lines)

for line in lines:
    print(line)
for line in lines:
    print(line.strip())