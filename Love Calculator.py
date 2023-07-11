#Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.lower()#to change the name in lower case
name2 = name2.lower()#to change the name in lower case
name=name1+name2
t=name.count('t')
r=name.count('r')
u=name.count('u')
e=name.count('e')
l=name.count('l')
o=name.count('o')
v=name.count('v')
e=name.count('e')
s1=t+r+u+e
print(s1)
s2=l+o+v+e
print(s2)
score=int(str(s1) + str(s2))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
