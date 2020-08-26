'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''


def main():
  num = int(input("Enter a number: "))

  print("These numbers are divisors of " + str(num) + ":")

  for x in range(1,num+1):
      print(x) if num % x == 0 else None
  
if __name__ == '__main__':
  main()