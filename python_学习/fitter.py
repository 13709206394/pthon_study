# filter() 函数用于过滤序列，接收一个函数和序列，返回值是true和false，决定保留还是丢弃该元素

# 在一个list中删除偶数，只保留奇数

def is_odd(n):
    return n%2==1
L=list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
print(L)

def not_empty(s):
    return s and s.strip()
L =list(filter(not_empty,['A','','B',None,'C',' ']))
print(L)

#定义一个生成素数的方法

def _odd_iter():#从3开始的奇数序列
    n=1
    while True:
        n=n+2
        yield n
def _not_divisiable(n):#定义一个筛选函数
    return lambda x: x%n>0

def primes():#定义一个生成器，不断返回下一个素数
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n = next(it) #返回序列的第一个数
        yield n
        it = filter(_not_divisiable(n),it)
for i in primes():
    if i<1000:
        print(i)
    else:
        break

def is_palindrome(n):
    L=list(str(n))
    for i in range(len(L)+1):
        if L[i]==L[-1-i]:
            return True
        else:
            return False
    # m=str(n)
    # if m[::]==m[::-1]: #使用字符串翻转的形式（切片）：
    #     return True
    # else:
    #     return False

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')