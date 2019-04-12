
def ooxx():
    fib = [0, 1]
    n = int(input('请输入长度: '))

    for i in range( n - 2):
        fib.append(fib[-1] + fib[-2])
    # print(fib)
    return fib  #函数运算的结果需要使用return返回值,否则None

mysql_list = ooxx()
print(mysql_list)
new_list = [10 + i for i in mysql_list]
print(new_list)
#
# ooxx()
# ooxx()
# ooxx()