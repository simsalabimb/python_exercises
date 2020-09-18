'''
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
'''

def reverse_sentence(sentence):
    phrase = sentence.split()
    phrase.reverse()
    return " ".join(phrase) 

def main():
  word = input("Give me a sentence to reverse: ")
  result = reverse_sentence(word)
  print(result)

if __name__ == '__main__':
  main()