import random
print("""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
""")
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")

dlevel=input("""Choose a difficulty. Type 'easy' or 'hard':""")
n=0

if dlevel=='easy':
  n=10
elif dlevel=='hard':
  n=5
else:
  print("Please give a valid input")
  ###

print(f"You have {n} attempts remaining to guess the number.")
a=random.randint(0,101)
print(f"answwr is {a}")
def game():
 global x
 x=int(input("Make a guess: "))
 def check():
  global n
  if n != 0:
  
    if x==a:
      print(f"You got it! The answer was {a}.")
    elif x>a:
      
      n=n-1
      print("""Too high.
      Guess again.""")
      print(f"You have {n} attempts remaining to guess the number.")
      game()
    elif x<a:
      n=n-1
      print("""Too low.
      Guess again.""")
      print(f"You have {n} attempts remaining to guess the number.")  
      game()
 check()
game()