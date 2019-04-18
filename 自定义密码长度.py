import random
list = []
def passwd(num):
    for i in range(int(num)):
        a = random.randrange(0,int(num))
        if i == a:
            b1 = random.randint(0,9)
            list.append(str(b1))
        else:
            b2 = chr(random.randint(65,90))
            list.append(b2)
    b3 = ''.join(list)
    return b3


if __name__ == '__main__':
    num = input('生成的密码长度为: ')
    password = passwd(num)
    print(password)