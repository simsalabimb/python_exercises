'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new 
list of only the first and last elements of the given list. 
For practice, write this code inside a function.
'''

def main():

  def grab_ends(a):
      return print(a[0],a[-1])

  #Get list of numbers from user input
  a = [int(x) for x in input().split()]
  grab_ends(a)

  
if __name__ == '__main__':
  main()