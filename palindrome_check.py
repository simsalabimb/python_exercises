'''
Ask the user for a string and print out whether this string is a palindrome or not.
'''


def main():
  text = input("Enter a word or sentence: ")
  #Account for spaces in words and make everything lowercase
  text = text.replace(" ", "").lower()

  if text == text[::-1]:
      print("{} is a palindrome".format(text))
  else:
      print("{} is NOT palindrome".format(text))

  
if __name__ == '__main__':
  main()