print('Welcome')
  print('I\'m watching you')
 print('Kindly dont delete any code')
    a = input('Do you want to play game? y for Yes n for No :')

 move = [1, 2, 3, 1, 4, 5, 6, 7]
    print(y in a)
   move.sort()
    print(sorted(move
    print(move)
   move.reverse()
   print(move)

   print(list(range(100)))

  a = ' X '.join(['a', 'b', 'c'])
 print(a)

 SIYA77 CODE
 import math
 c = math.factorial(5)
 d = math.pow(5,2)
 e = math.sin(1)
 print(c)
 print(d)
 print(e)
 Other ways of doing factorial is by using for loop or recurssion

 a,b,c, *other, d,e = [1,2,3,1, 4, 5, 6, 7]
 print(a)
 print(b)
 print(c)
 print(d)
 print(e)

 Dictionary
 di = [{
   'a' : 1,
   'b' : 2,
   'c' : [1, 2, 3, 7]
 },
 {
   'a' : 1,
   'b' : 2,
   'c' : 3
 }]

 print(di[0]['c'][3])
 print(di[1]['b'])

 list is sorted, dictionary is not sorted
 Dictionary must be immutable

 di = {
   'name' : 5,
   'age' : 5,
   'code' : 10
 }

 print(di.get('comb'), 50)

 di = dict(name = '5', age = '6')
 print(di['age'])

 print('age' in di)

  print('name' in di.keys())
   print('5' in di.values())
   print(di.items())
  di1 = di.copy()
  di.clear()
  print(di)

   print(di1)

   print(di.pop())
  it wont remove last item of Dictionary as its not sorted

  di.update({'age' : 25})
  print(di)
  di.update({'names' : 50})
   print(di)

  input('a=')
  input('b=')
 mat0 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
 mat1 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
 mat2 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
 print('SUDOKU')
 print('=====================================')
 print(' ', mat0[0][0], ' ', mat0[1][0], ' ', mat0[2][0], ' ')
 print(' ', mat0[0][1], ' ', mat0[1][0], ' ', mat0[2][0], ' ')
 print(' ', mat0[0][2], ' ', mat0[1][0], ' ', mat0[2][0], ' ')
 print(' ')
 print(' ', mat1[0][0], ' ', mat1[1][0], ' ', mat1[2][0], ' ')
 print(' ', mat1[0][1], ' ', mat1[1][0], ' ', mat1[2][0], ' ')
 print(' ', mat1[0][2], ' ', mat1[1][0], ' ', mat1[2][0], ' ')
 print(' ')
 print(' ', mat2[0][0], ' ', mat2[1][0], ' ', mat2[2][0], ' ')
 print(' ', mat2[0][1], ' ', mat2[1][0], ' ', mat2[2][0], ' ')
 print(' ', mat2[0][2], ' ', mat2[1][0], ' ', mat2[2][0], ' ')
 print('=====================================')
 print(' ')

  Conditional logics

  Location = 'Earth'
  Location1 = 'Asia'
  Location2 = True
  Location3 = False
  if Location:
    print('You are from Earth!!')
    if Location1:
      print('Youre from Asia!!')
      if Location2:
        print('Youre from India')
        if Location3:
          print('Youre from Delhi')
        else:
          print('Not Dellite, Get Lost!! :-)')
      else:
        print('Youre not from India!!')
   else:
     print('Youre not from Asia!!')
 else:
   print('Youre not human!!')
   print('GOGOGOGOGO')

   if Section2:
     print('You can play low level game!!')
   else:
     print('You are not eligible!!')


 Terniary operator

  drink = True
  drunk = False
   buy = 'can drink' if drink else 'cannot drink'

   print(buy)


  if drink and drunk:
    print('Player drunk')

 logical operator
  ==
 a = input('You want to play game? Y for Yes :')
  print(a == 'y' or a == 'Y')
 if a == 'y' or a == 'Y':
   print('You can play Game!')
  else:
    print('Get Lost!!')

  a = input('Input anything : ')
  if not a:
    print('Get lost!!')

 magic = False
 expert = True

 if magic and expert:
   print('Good')
 elif magic and not expert:
   print('Learning')
  elif not magic:
    print('Learn magic')
  else:
    print('Get lost!!') 

 print(True is 1)
  is compares the value of text by address
 print(1 == True)
  == compares the value of text irrespective of address



LOOPS
 DIGITAL CLOCK
 import os #this lib for using clear function
 import time #this lib for using sleep function

 a = range(0,24)
 b = range(0,60)
 c = range(0,60)
 for d in range(0, 365):

   for hour in a:
     for minutes in b:
       for seconds in c:
         print('DIGITAL CLOCK')
         print('Hours   : ', hour, '\nMinutes : ', minutes, '\nSeconds : ', seconds)
         time.sleep(1)
         os.system('clear')
         while True:
         if(input()==""):
          print('x')
         else:
            print('y')
         time.sleep(1)



       we dont want that line printing every second  
          z = input('do u want to stop? enter 1')

        
          if(input()):
            print('Hours   : ', hour, '\nMinutes : ', minutes, '\nSeconds : ', seconds)
            time.sleep(1)
            os.system('clear')

 if(not input()):
          print('x')
 else:
            print('y')



 LOOP why did you delete everything
