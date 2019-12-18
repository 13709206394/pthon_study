#列表生成器一：
# g = (x*x for x in range(11))
# print(next(g))
#
# for n in g :
#     print(n)

# n,a,b=1,2,3
# print('n'+'=',n)
# print('a'+'=',a)

# def fib(max):
#     n,a,b =0,0,1
#     while n <max:
#         print(b)
#         a,b=b,a+b
#         n = n+1
#     return 'done'
# print(fib(6))


# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done'
# print(next(fib(6)))
# g = fib(6)
# while True:
#     try:
#         x=next(g)
#         print('g:',x)
#     except StopIteration as e:
#         print('Generation return value:',e.value)
#         break
#使用for循环调用generator时拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获
#StopIteration错误，返回值包含在StopIteration的value中：

# def odd():
#     print('step 1')
#     yield 1
    # print('step 2')
    # yield 3
    # print('step 3')
    # yield 5
# o=odd()  生成器函数从next（）开始执行，遇到yield停止
# next(o)
# next(o)
# next(o)

# def triangles():
#     p=[1]
#     while True:
#         yield p
#         p =[1] +[p[i]+p[i+1] for i in range(len(p)-1)]+[1]
#
# n=0
# for t in triangles():
#     print(t)
#     n=n+1
#     if n==10:
#         break

# 利用 map 和 reduce 编写一个 str2float 函数 ， 把 字符串 ‘123.456’
# 转换成浮点数’123.456’

from functools import reduce
def str2float(s):
    def fn(x,y):#数字拼接
        return x*10+y
    n =s.index('.')#分割字符串
    num_int=list(map(int,[x for x in s[:n]]))#整数部分
    num_float=list(map(int,[x for x in s[n+1:]]))#小数部分
    return reduce(fn,num_int)+reduce(fn,num_float)/10**len(num_float)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


