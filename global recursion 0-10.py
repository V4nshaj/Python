i=0
def sum(n):
    global i
    if i!=10:
        i=i+1
        return sum(n+i)
    else:
        return n
num=sum(0)
print(num)