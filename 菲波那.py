# a = 'hello'
# b = ['bob', 'client']
# c = ('10', '20')
# d = {'name': 'tom', 'age': '21', 'email': 'qq.com'}
# for i in a:
#     print(i)
# for i in b:
#     print(i)
# for i in c:
#     print(i)
# for i in d:
#     print('%s: %s' %(i, d[i]))
# range(10)
# range(0,10)
#
# for i in range(10):
#     print(list(range(i)))

fib = [0, 1]
n = int(input('请输入长度: '))

for i in range( n - 2):
    fib.append(fib[-1] + fib[-2])
print(fib)