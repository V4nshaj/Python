#game rock paper and scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#code
comp = random.randint(0,2)
l1 = [rock, paper, scissors]
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")) 
print(l1[user])
print("Computer chose:")
print(l1[comp])
print(comp)
if user==comp:
    print("it's a draw")
elif (user== 2 and comp==0) or (user== 0 and comp==1) or (user== 1 and comp==2):
    print("You lose")
elif (user== 0 and comp==2) or (user== 1 and comp==0) or (user== 2 and comp==1):
    print("You Win")