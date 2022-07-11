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

img=[rock, paper, scissors]
p=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(img[p])
c=random.randint(0,2)
print(f"Computer chose {img[c]}")

if p==0 and c==2:
  print("You win!")
elif p==2 and c==0:
  print("You lose!")
elif p>c:
  print("You win!")
elif p==c:
  print("It's a draw")
elif p>=3 or p<0:
  print("Invalid input.")




