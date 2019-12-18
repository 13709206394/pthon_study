# try:
#     print('try...')
#     r=10/2
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r=10/int('a')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:',e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')

# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#         print('pass')
#     except Exception as e:
#         print('Error: %s',e)
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
#
# main()

# Python内置的logging模块可以非常容易地记录错误信息：
# import logging
# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s)*2
# def main():
#     try:
#         bar('s')
#     except Exception as e:
#         logging.exception(e)
# main()
# print('END')

# def foo(s):
#     n=int(s)
#     if n==0:
#         raise ValueError('invalid value:%s'%s)
#     return 10/n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#
# bar()

# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复
from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except Exception as e:
        print('Exception:%s',e)

main()






