class book:
    def __init__(self, tittle,author):
        self.tittle = tittle
        self.author = author

    def __str__(self):
        return '<<%s>>' % corepy.tittle

    def __call__(self):
        print('%s is written by %s' % (self.tittle, self.author))

if __name__ == '__main__':
    corepy = book('运维之道', '小丁') #调用__init__方法
    print(corepy)   #打印实例时,自动调用__str__方法
    corepy()        #自动调用__call__方法,是实例像函数一样,可以调用
