# import os
# import time
# import random

# a = []
# ex = True
# count = 0
# # if (input('Do you want to play? Y/N') == 'y' or 'Y'):
# #     print('Game Began!!!')
# # else:
# #   goto z;
# while (ex):

#     for i in range(5):
#         n = random.randint(10, 100)
#         a.append(n)
#     print(*a, sep=' ')
#     if count < 10:
#         time.sleep(2)
#     if count >= 10 and count < 20:
#         time.sleep(1)
#     os.system('clear')
#     b = input('Enter the largest number : ')
#     x = int(b)
#     if max(a) == x:
#         ex = True
#         count += 1
#     else:
#         ex = False
#         print('You made mistake!!')
#     a.clear()
# # z:
# if ex:
#     print('Your score is : ', count)
# else:
#     print('Your score is : 0')



### **alpha** MIND GAME *give a try*###
import random #to get random numbers
import os #to clear the output display
import time #to delay the process 
def solve(x,li1):
    my_randoms = []

    for i in range(x):
        my_randoms.append(random.randrange(10, 101, 1))#To append random number 
    print(*my_randoms)
    time.sleep(li1)
    os.system('clear')
    return max(my_randoms)
a = 5
li=1
count = 0
print('GAME FOR MAXIMUM NUMBER DETECTION!!!\n')
time.sleep(5)
os.system('clear')
print('GET READY!!\n')
time.sleep(3)
os.system('clear')
print('GO!!!\n')
time.sleep(2)
os.system('clear')
while True:
   
    l = solve(a,li)
    i=int(input("WHATS YOUR ANSWER : "))

    if i==l:#If ans is crt this block will be executed
        
        print('''good job!...you won''')
       
        time.sleep(1)
        os.system("clear")
        time.sleep(1)
        a+=1
        count+=1
    else:#If ans is worng this will be executed
        os.system("clear")
        print("sorry!!..you lose\n")
        print("but nice try!!..\n")
        print("YOU SCORE :",count)
        break       

    if count<10 and count%3==0:#For every 3 rounds disply time will be increased by .5 seconds
        print('Bonus time added!!')
        time.sleep(1)
        os.system('clear')
        li+=.5

