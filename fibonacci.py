'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
'''

def fib_generator(x):
  if x == 0:
    fibs=[]
  elif x == 1:
    fibs=[1]
  elif x == 2:
    fibs=[1,1]
  else:
    fibs=[1,1]
    while len(fibs) < x:
      fibs.append(fibs[-1]+fibs[-2])

  return fibs  


def main():
  num = int(input("How many numbers of the fibonacci sequence do you want me print out?"))
  print(num)

  print(fib_generator(num))

  
if __name__ == '__main__':
  main()