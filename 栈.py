stack = []

def push_it():
    item = input('内容: ').strip()
    if item:
        stack.append(item)

def pop_it():
    if stack:
        print('从栈中弹出: %s' % stack.pop())
    else:
        print('空栈')

def view_it():
    print('\033[31;1m%s\033[0m' % stack)

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    promat = '''
    (0) 压栈
    (1) 出栈
    (2) 查询
    (3) 退出
    请选择(0/1/2/3): '''

    while True:
        choice = input(promat).strip()[0]
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入,请输入正确的序列号: ')
            continue
        if choice == '3':
            print('滚')
            break

        cmds[choice]()
        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # elif choice == '2':
        #     view_it()
        # else:
        #     print('滚')
        #     break

if __name__ == '__main__':
    show_menu()