import time
import os
mat = [[[
  [0, 2 ,0], # # X 2 X   X X 4   3 X X
  [0, 0, 4], 
  [3, 0, 0]    
],
[
  [9, 0 ,0],# # 9 X X   X 2 X   X X 8
  [0, 2, 0],
  [0, 0, 8]
],
[
  [0, 0 ,0],# # X X X   6 X 9   X 5 X 
  [6, 0, 9],
  [0, 5, 0]
]],
[[
  [0, 0 ,0],# # X X X   X X X   X X 1
  [0, 0, 0],
  [0, 0, 1]
],
[
  [0, 7 ,2],# # X 7 2   5 X 3   6 8 X
  [5, 0, 3],
  [6, 8, 0]
],
[
  [6, 0 ,0],# # 6 X X   X X X   X X X
  [0, 0, 0],
  [0, 0, 0]
]],
[[
  [0, 8 ,0],# # X 8 X   2 X 5   X X X
  [2, 0, 5],
  [0, 0, 0]
],
[
  [1, 0 ,0],# # 1 X X   X 9 X   X X 3
  [0, 9, 0],
  [0, 0, 3]
],
[
  [0, 0 ,9],# # X X 9   8 X X   X 6 X
  [8, 0, 0],
  [0, 6, 0]       
]]  
]

result_mat = [[[
  [8, 2 ,7],
  [1, 5, 4],  
  [3, 9, 6]    
],
[
  [9, 6 ,5],
  [3, 2, 7],
  [6, 1, 8]
],
[
  [3, 4 ,1],
  [6, 8, 9],
  [7, 5, 2]
]],
[[
  [5, 9 ,3],      
  [4, 6, 8],
  [2, 7, 1]
],
[
  [4, 7 ,2],
  [5, 1, 3],
  [6, 8, 9]
],
[
  [6, 1 ,8],
  [9, 7, 2],
  [4, 3, 5]
]],[
[
  [7, 8 ,6],
  [2, 3, 5],
  [9, 1, 4]
],
[
  [1, 5 ,4],
  [7, 9, 6],
  [8, 2, 3]
],
[
  [2, 3 ,9],
  [8, 4, 1],
  [5, 6, 7]       
]]]

m = 'y'
QW=True

while(QW):
  print('\t\tSUDOKU PUZZLE\n')
  for a in range(3):
    for b in range(3):
      for c in range(3):
        print(mat[a][b][c], end ='   ')
      print('\n')
    print('\n')
  m = 'y'
  while m == 'y' or m == 'Y': 
    print('Do you want to change an item?')
    m = input('(Y/y for yes,N/n for no) : ')
    if m == 'y' or m == 'Y':   
      w = input('Enter row of matrix (0 to 2): ')
      x = input('Enter column of matrix (0 to 2): ')
      y = input('Enter row of value (0 to 2): ')
      z = input('Enter column of value (0 to 2): ')
      item = input("input the new value : ")
      w = int(w)
      x = int(x)
      y = int(y)
      z = int(z)
      item = int(item)
      mat[w][x][y][z] = item
      os.system('clear') 
      for a in range(3):
       for b in range(3):
         for c in range(3):
          print(mat[a][b][c], end ='   ')
         print('\n')
       print('\n') 
    k = input('do you want to submit your code? ')
    if(k == 'y' or k == 'Y'): 
      QW= False
      m = 'n'
    if(k == 'n' or k == 'N'):
      QW = True
      m = 'y'
    else:
      print("ENTER A PROPER VALUE USER!")   
print('Awaiting result. . . ')
if mat == result_mat:
  
  os.system('clear')
  print("YAY! you win!")     
else:
  os.system('clear')
  print("Try Again")


  import os

