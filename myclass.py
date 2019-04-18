class A:
    def fun1(self):
        print('a  func')
    def fun(self):
        print('aaaaaaaa')

class B:
    def fun2(self):
        print('b func')
    def fun(self):
        print('bbbbbb')

class C(B,A):
    def fun3(self-):
        print('c func')

    def  fun(self):
        print('ccccccc')
if __name__ == '__main__':
    c1 = C()
    c1.fun1()
    c1.fun2()
    c1.fun()
