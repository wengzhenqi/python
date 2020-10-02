import random
import string

# cc = 0
# while 1:
#     for i in range(20):
#         str = (string.ascii_uppercase + string.digits)          #全部的大写字母和数字
#         a = random.sample(str, 5)                   #随机生成5个字符
#         b = "".join(a)                              #因为拼接出来的是列表，使用join方法拼接成整体
#         m = string.ascii_uppercase                  #随机大写
#         n = random.choice(m)
#         pai = ("京"+n,b)
#         print(pai)
#         # yong = input("请输入您的选择： ".strip(""))
#         # if yong ==
#
#     cc +=1

    # if cc == 3:
    #     break

cc = 0
while cc < 3:
    car_nums = []
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)      #生成车牌的第一个字母
        n2 = "".join(random.sample(string.ascii_uppercase + string.digits,5))    #生成车牌的后面字符
        c_nums = "京" + n1 +" " + n2
        car_nums.append(c_nums)
    print(car_nums)

    yong = input("请输入你的选择： ".strip(""))
    if yong in car_nums:
        print(f"恭喜您获得了 {yong} 牌照")
        break
    else:
        print("您的输入不合法。。。")

    cc +=1

