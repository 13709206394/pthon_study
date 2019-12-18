# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax=ax+n
#         return ax
#     return sum #返回
# f1=lazy_sum(1,3,5,7,9)#调用lazy_sum()时，返回的是求和函数
# f2=lazy_sum(1,3,5,7,9)
# print(f1==f2)
# print(f1)
# print(f2)
# print(f1())
# print(f2())
#
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print(f1(),f2(),f3())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    s = [0]
    def counter():
        s[0]=s[0]+1
        return s[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')