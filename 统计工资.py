import os
import pickle
from time import strftime

def save(fname):
    amount = int(input('金额: '))
    comment = input('说明: ')
    date = strftime('%y-%m-%d')
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)
        balance = data[-1][-2] + amount

    line = [date, amount, 0, balance, comment]
    data.append(line)

    with open(fname, 'wb') as fobj:
        pickle.dump(data, fobj)


def query(fname):
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)
    print('%-15s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    for line in data:
        print('%-15s%-8s%-8s%-12s%-20s' % tuple(line))  # 将列表转成>元组

def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = '''(0) 收入
(1) 支出
(2) 查询
(3) 退出
请选择(0/1/2/3)'''
    fname = 'record.data'
    if not os.path.exists(fname):
        date = strftime('%y-%m-%d')
        data = [
            [date, 0, 0,10000, 'init data']
        ]
        with open(fname, 'wb') as fobj:
            pickle.dump(data, fobj)

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入,请重试')
        if choice == '3':
            print('拜拜')
            break
        cmds[choice]()

if __name__ == '__main__':
    show_menu()
