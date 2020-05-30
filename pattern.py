# a = [1, 2, 3, 4, 5]
# s = " "
# for i in range(1, 5):
#   for j in a:
#     print (s + a)
#     a = a.pop()

def pattern(var)
  lis=[]
  for i in range(max(var)):
    lis.append(i)
    for tot in var:
      if tot in lis:
        continue
      else:print(tot,end=" ")
    print()
  for i in range(max(var)-1,0,-1):
    lis.remove(i)
    for j in var:
      if j in lis:
        continue
      else: print(j,end=" ")
    print()
a=int(input("give some number : "))
lis=list(range(a,0,-1))+list(rnage(2,a+1)


# #PYTHON  :)
# #LOOPS
# #PATTERNS

# #first pattern you give and i code then i give you code
# # 54321
# # 4321
# # 321
# # 21
# # 1

# #u give me the pattern now, 
# # I will think until then
# # 54321
# #  4321
# # #   321
# # #    21
# # #     1  

# # # import math
# # # a = 54321
# # # for b in range(0,5):
# # #   print(a)
# # #   a = a% pow(10,5-b-1)

# # #done haha
# # #your turn

# # import math
# # a = 54321
# # for b in range(0, 5):
# #     print (b * " ", a)
# #     a = a% pow(10,5-b-1)
    

#     #loops in python is confusing
#     # sorry got confused with variables haha
#     # atleast you got it
#     #it's easy, if you think how your code run in mind
# #let's try some hard one?

# # #WOLF PATTERN
# # 543212345
# # 5432 2345
# # 543   345
# # 54     45
# # 5       5
# # 54     45
# # 543   345
# # 5432 2345
# # 543212345
# #easy one for you:-) THIS IS NOT AT ALL EASY!!haha

# # 33333
# # 32223
# # # 32123
# # # 32223
# # # 33333 

# # # Try to do this
# # #this one good
# # import math
# # a = [3,3,3,3,3] 
# # b = int(len(a))
# # m = int(b/2)
# # d=e=f = 1

# # for c in range(0, m+1):
# #   print(a)
# #   a[1] = a[1] - d
# #   a[2] = a[2] - e
# #   a[3] = a[3] - f
# #   d=0
# #   f=0

# # e+=1
# # for c in range(0, m):

# #   a[1] = a[1] + d
# #   a[2] = a[2] + e
# #   a[3] = a[3] + f
  
# #   print(a)
# #   d+=1
# #   e-=1
# #   f+=1

# # did you made code already?

# # 543212345
# # 5432 2345
# # 543   345
# # 54     45
# # 5       5
# # 54     45
# # # 543   345
# # # 5432 2345
# # # 543212345
# # import os
# # # shall i do this one?
# a = [5, 4, 3, 2, 1]
# b = [2, 3, 4, 5]
# x = 5
# y = 0
# z=0
# b1 = b
# # for j in range(4)
# # for i in range(5):
# #   print(a[i], end = ' ')
# # print(a[5-i], end = ' ')
# for m in range(9):
#  for i in range(x):
#   print(a[i], end=' ')
# #  if y==0:     #this loop i need to print one extra time to fix first row
# #    for j in range(y,4):
# #     print(b[j], end = ' ')

#  for n in range(z):
#    print(n * ' ', end=' ')  
#  for j in range(1):
#   print(b[j], end = ' ')
#  for j in range(y,4):
#   print(b1[j], end = ' ')
#  print('\n')
#  x-=1
#  z+=1
#  y+=1

# # os.system('clear')
# # print('x', end=' ') or print('y') or print('z')






# # 543212345
# # 5432 2345
# # 543   345
# # 54     45
# # 5       5
# # 54     45
# # 543   345
# # # 5432 2345
# # # 543212345

# # for i in range(5,0,-1):
# #   # for g in range(1,6):
# #     print(*list(range(i,0,-1)))

m = 0
n = 2
p = 0
count=0
for a in range(5):
  for a in range(5,m,-1):
   print(a, end=' ')
  if count<1:
   for a in range(n,6):
     print(a, end=' ')
  # if count<1:
  #   n=2
  if count>=1:
    print(' ' * p, end=' ')
  if count>=1:
   for a in range(n,6):
    print(a, end=' ')
  print('\n')
  m+=1
  if count>=1:
    n+=1
    p+=4
  else:
    p+=1
  count+=1
m=3
n=4
p=9
for a in range(5):
  if m>=0:
    for a in range(5,m,-1):
     print(a, end=' ')
  m-=1
  if count>1:
    print(' ' * p, end=' ')
  count-=1
  if count>1:
    for a in range(n,6):
     print(a, end=' ')
  if count==1:
    n=2
    for a in range(n,6):
     print(a, end=' ')
  n-=1
  p-=4
  print('\n')


# *alpha*diamond pattern code***  
# def pattern(var):
#   lis=[]
#   for i in range(max(var)):
#     lis.append(i)
#     for tot in var:
#       if tot in lis:
#         print(" ",end=" ")
        
#       else:print(tot,end=" ")
#     print()
#   for i in range(max(var)-1,0,-1):
#     lis.remove(i)
#     for j in var:
#       if j in lis:
#         print(" ",end=" ")
       
#       else: print(j,end=" ")
#     print()
# a=int(input("give some number : "))
# lis=list(range(a,0,-1))+list(range(2,a+1))
# pattern(lis)

   
   
   
   
  #  problem is, the second loop need to be printed twice, in row 1 and row 2
#cool



