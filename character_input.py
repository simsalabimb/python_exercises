'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
import datetime


def main():
  name = input("What is your name? ")
  age = int(input("How old are you? "))

  year = datetime.date.today().year
  age_100 = (year - age) + 100
  
  print("You will be 100 in the year: " + str(age_100))

  
if __name__ == '__main__':
  main()