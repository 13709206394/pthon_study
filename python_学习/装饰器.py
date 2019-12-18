# import time
# def now():
#     print('2019-10-18')
# f=now
# print(f())

#__name__属性，可以拿到函数的名字
# print(now.__name__)
# print(f.__name__)

def log(func):
    def wrapper(*args,**kwargs):
        print('call %s():'%func.__name__)
        return func(*args,**kwargs)
    return wrapper()
@log
def now():
    print('2019-10-18')
f=now
# print(f())

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        start=time.time()
        func=fn(*args,**kwargs)
        end=time.time()
        print('%s executed in %s ms' % (fn.__name__, (end-start)*1000))
        return func
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')