'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only 
the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''


def main():
  
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

  common_list = []

  my_set = set(a)
  a = list(my_set)

  for x in a:
      if x in b:
          common_list.append(x)

  print(common_list)

  
if __name__ == '__main__':
  main()