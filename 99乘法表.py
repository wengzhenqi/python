# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()
# #
# for i in range(3):# i 控制打印几行
#     for j in range(3):#内层循环控制一行内打印几次hello
#         print('hello', end='  ')#print默认在结尾打印\n, 将结尾修改为空格
#     print()
for i in range(1, 10):
    for j in range(1, i+1):
        print('%s*%s=%s ' % (i, j, i*j), end='')
    print()