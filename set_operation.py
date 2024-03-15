seta = {1,2,3,4,5}
setb = {4,5,6,7,8}

print(seta | setb)#union of set
print(seta & setb)#intersection of set
print(seta - setb)
print(setb - seta)
print(setb ^ seta)

seta.add(10)
seta.remove(20)#does cause error
seta.discard(20)#doesnt show error