# ou = []
# li = []
# for i in range(100):
#     if  i % 2 == 0:
#         print(f"{i} 是偶数")
#         ou.append(i)
#     elif i % 2 != 0:
#         print(f"{i} 是奇数")
#         li.append(i)
# print(ou,li)



# for i in range(1,6):
#     print(f"---------------------{i}层---------------------")
#     for j in range(10):
#         print(f"第{i}层的第{j}个房间")

# for i in range(1,6):
#     print(f"---------------------{i}层---------------------")
#     if i == 3:
#         print("="*10)
#         continue          #跳过本次，进入下一次
#     for j in range(10):
#         print(f"第{i}层的第{j}个房间")

# for i in range(1,6):
#     print(f"---------------------{i}层---------------------")
#     for j in range(10):
#         if i == 4 and j == 4:
#             print("404房间over")
#             break       #结束本次循环
#         print(f"第{i}层的第{j}个房间")


# for i in range(1,10):
#     if i <= 5:
#         print("*" * i)
#     else:
#         print((10 - i) * "*")
# a = 0
# block_girl_age = 26
# while 1:
#     alex = int(input("请输入您猜的数: ").strip())
#     if alex > block_girl_age:
#         print("猜大了")
#     elif alex < block_girl_age:
#         print("猜小了")
#     else:
#         print("猜对了")
#         break
#
# print(f"总共猜了{a}次")



# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}",end = ' ')
#     print( )


#
# for i in range(1,10):
#     for j in range(1,i+1):
#        print(f"{i}*{j}={i+j}",end = ' ')
#     print()




#牌照摇号小程序
# import random
# while 1:
#     a = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")        #生成一个随机数
#     print(a)
#
#     if a == "c":
#         break

# import random
# import string
# str = (string.ascii_uppercase + string.digits)        #全部的大写字母和数字
# a = random.sample(str,5)                            #随机生成5个字符
# b = "".join(a)                                      #因为拼接出来的是列表，使用join方法拼接成整体
# # print(b)
# m = string.ascii_uppercase
# n = random.choice(m)
# for i in n:
#     print("京"+n,b)



