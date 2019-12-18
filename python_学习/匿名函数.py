'''关键字lambda表示匿名函数，冒号前面的x表示函数参数。
1.匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
2.匿名函数也是一个函数对象，可以把匿名函数赋值给一个变量，再利用变量来调用该函数
3.匿名函数也可以作为返回值返回

'''
L=list(map(lambda x:x*x,[1,2,3,4,5]))
print(L)

fn=lambda x:x*x
print(fn)
print(fn(2))

def build(x,y):
    return lambda :x*x+y*y
print(build(2,3)())

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)