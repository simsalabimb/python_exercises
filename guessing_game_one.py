'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.'''

import random

def main():
  num = random.randint(1,9)
  correct = False
  print(num)

  while correct == False:
      
      guess = int(input("What's the number? \n"))

      if guess == num:
          print("You got it right!")
          break
      elif guess < num:
          print("A little too low :(")
      else:
          print("Too High!")

  
if __name__ == '__main__':
  main()