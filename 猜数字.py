from random import randint, choice

def add(x,y):
    return x + y

def sub(x,y):
    return  x - y

def exam():
    cmds = {'+': lambda x,y:x + y, '-':lambda x,y: x-y}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  #降序排列,默认升序
    op = choice("+-")

    result = cmds[op](*nums)    #将列表拆开

    prompt = '%s %s %s = ' % (nums[0], op, nums[1])   #算式

    counter = 0
    while counter < 3:
        try:

              answer = int(input(prompt))
        except:
            print()
            continue
        if answer == result:
            print('牛逼牛逼,大佬牛逼')
            break

        print('差一丢丢哦')
        counter +=1

    else:
        print('%s%s' %(prompt,result))

def main():
    while 1:
        exam()
        try:
             yn = input ('Continue(y/n)?').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        if yn in 'Nn':
            print('拜拜')
            break


if __name__ == '__main__':
    main()