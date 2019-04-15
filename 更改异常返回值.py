try:
    num = int(input('number: '))
    result = 100 / num
    print(result)

except ValueError:
    print('无效的数字')
except EOFError:
    print('\n拜拜')
except ZeroDivisionError:
    print('无效的数字')
except KeyboardInterrupt:
    print('\n拜拜')