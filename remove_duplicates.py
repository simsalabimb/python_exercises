'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
'''

def main():
  lst = [1,2,4,5,2,9,10,8,8,8]

  lst_set = set(lst)  

  lst2 = []

  for i in lst:
      if i not in lst2:
          lst2.append(i)

  print(lst_set)
  print(lst2)

if __name__ == '__main__':
  main()