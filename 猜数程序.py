# import random
#
# answer = random.randint(1,100)
# print('猜数游戏')
# num = input("请输入你要猜测的数字1-100: ")
# guess = int(num)
# n = 0
# while n < 2:
#     if guess == answer and n ==0:
#         print('么么哒,对啦')
#         print('厉害了一次就对了')
#         break
#     if guess < answer:
#         print('不对哦,太小了')
#     elif guess > answer:
#         print('不对哦,太大了')
#     elif guess == answer:
#         print('么么哒,对啦')
#     n +=1
#     if n == 1 and guess == answer:
#         print('可以哦,第二次就答对了')
#         break
#     elif n ==2 and guess == answer:
#         print('还行,终于才出来了')
#         break
#     elif n == 2 and guess != answer:
#         print('不行哦,三次都不对')
# print('游戏结束')

import random
num = random.randint(1,20)
counter = 0
while counter < 3:
    counter +=1
    answer = int(input('请输入数字: '))
    if answer > num:
        print('猜大啦')
    elif answer < num:
        print("猜小啦")
    else:
        print('猜对啦')
        break
else:
    print('正确结果是: %s' % num)