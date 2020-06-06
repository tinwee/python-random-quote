import random

def primary():
#  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

#  last = 13
  last = len(quotes) - 1

#  for n in (0,1):
  for n in range(10):
#  for n in ['First', 'Second', 'Third']:
    rnd = random.randint(0, last)
#  print(quotes[13])
    print(n, last, rnd)
    print(quotes[rnd].strip())

if __name__== "__main__":
  primary()
