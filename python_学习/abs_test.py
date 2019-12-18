# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>=0:
#         return x
#     else:
#         return -x
# print(my_abs(-14))

# import math
#
# def move(x,y,step,angle=0):
#     nx = x +step * math.cos(angle)
#     ny = y -step * math.sin(angle)
#     return nx,ny
#
# x,y=move(100,100,60,math.pi/6)
# print(x,y)

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。

# 提示 计算平方根可以调用math.sqrt()函数：
# import math
# def quadratic(a,b,c):
#     if not isinstance(a or b or c,(int,float)):
#         raise TypeError('bad operand type')
#     elif b**2-4*a*c <0:
#         print("无解")
#     else:
#         x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
#         x2 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
#
#     return x1,x2
#
# x1=quadratic(2,3,1)
# x2=quadratic(1,3,-4)
# print(x1,x2)
#
# # 测试:
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')

# def move(n,a,b,c):
#     if n==1:
#         print(a,'-->',c) #将A上圆盘直接移到C
#     else:
#         move(n-1,a,c,b)  #当A上圆盘不止一个时，借助C将n-1个圆盘移动到B
#         print(a,'-->',c) #将A上剩余的最后一个圆盘，移到C
#         move(n-1,b,a,c) #借助A将,n-1个圆盘从B移动到C
# move(3,'A','B','C')

#请使用迭代查找一个list中的最大值和最小值，并返回一个tuple

# def findMinAndMax(L):
#     if L==[]:#判断L是否为空列表，为空则返回None
#         return (None,None)
#     elif len(L)==1:#判断L中的元素个数，只有1个元素则返回L[0]
#         return (L[0],L[0])
#     else:#当有多个元素时
#         min=L[0]
#         max=L[0]
#         for x in L:
#             if x <=min:
#                 min =x
#             if x >=max:
#                 max =x
#         return (min,max)
#
# print(findMinAndMax([]))
# print(findMinAndMax([0]))
# print(findMinAndMax([1,0,3,2,7]))
#
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

#要生成list[1,2,3,4,5,6,7,8,9,10]
# L=list(range(11))
# print(L)
#
# #[1x1, 2x2, 3x3, ..., 10x10]
#
# L=[]
# for x in range(11):
#     L.append(x*x)
# print(L)
#
# #列表生成式
# print([x*x for x in range(11)])
#
# #列表生成式，筛选偶数
# print([x*x for x in range(11) if x%2==0])
# #筛选奇数
# print([x*x for x in range(11) if x%2!=0])
#
# print([m+n for m in 'ABC' for n in 'XYZ'])
#
# import os
#
# print(d for d in os.listdir('.'))

d={'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])

# 大写字母变为小写
L=['Hello','World','IBM','Apple']

# for i in range(len(L)):
#     L[i]=L[i].lower()
# print(L)

print([s.lower() for s in L])
















