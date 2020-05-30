import os
import time
import random

a = []
ex = 0
if ex < 20:
  for i in range(5):
    n = random.randint(10,100)
    a.append(n)
  print(*a, sep = ' ')
  if ex < 10:
    time.sleep(2)
  if ex >= 10 and ex <20:
    time.sleep(1)
  os.system('clear')
  b = input('Enter the largest number : ')
  x = int(b)
  if max(a) == x:
    ex+= 1
  else:
    print('You made mistake!!')
   
if ex:
  print('Your score is : ', ex)
else:
  print('Your score is : 0')