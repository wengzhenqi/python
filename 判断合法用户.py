while True:
    a = input('请输入账户: ')
    b = input('请输入密码: ')
    if a == "bob" and b == '123456':
        print('正确')
        break
    else:
        print("错误")