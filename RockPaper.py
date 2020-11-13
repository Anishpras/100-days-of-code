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

list = [rock, paper, scissors]

humanChoice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
print(list[humanChoice])

print("Computer Chose :")
computerChoice = random.randint(0, 2)
print(list[computerChoice])

if humanChoice == computerChoice:
    print("Draw")
elif humanChoice == 0 and computerChoice == 2:
    print("you win")
elif computerChoice > humanChoice:
    print("You Lose")
else:
    print("You win")

