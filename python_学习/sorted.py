#sorted()函数可以对list进行排序
print(sorted([36,15,-5,-30,45]))
print(sorted([36,5,-12,9,-21],key=abs))
# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))#忽略大小写进行字符串排序
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))

# 请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0]
# def by_score(t):
#     return t[1]
def by_name(t):
    for x in t:
        if isinstance(x,str):#判断s是否可迭代
            return x

def by_score(t):
    for x in t:
        if isinstance(x,int):
            return -x


L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)