# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# height = float(input("请输入身高："))
# weight = float(input("请输入体重："))
# bmi = weight/(height*height)
# print(bmi)
#
# if bmi <18.5:
#     print("过轻")
# elif bmi <=25:
#     print("正常")
# elif bmi <=32:
#     print("过重")
# else:
#     print("严重肥胖")


# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
#
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print("Hello,%s!"%name)
#
# s1=72
# s2=85
# r=(s2-s1)*100/s1
# print('小明成绩提升了%.1f%%'%r)
#
# print('小明成绩提升了{:.1f}%'.format(r))


# t=(1)  #定义只有一个元素的元组，要交逗号
# p=(1,)
# print(type(t))
# print(type(p))
#
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]

# 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])

# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')

# birth = int(input('birth'))#input 返回类型为str
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# 1-100累加求和
# sum = 0
# for x in list(range(101)):
#     sum = sum +x
# print(sum)
#range()可以生成一个整数序列，list（）函数可以转换为list


#使用while循环计算100以内的奇数之和

# sum = 0
# i=99
# while i > 0:
#     sum = sum +i
#     i = i - 2
# print(sum,i)

# 打印1~100的数字
# i =0
# while i<100:
#     # if i >10:#当i=11的时候，执行break，循环提前结束
#     i = i+1
#     if i%2==0:#判断是否为偶数，是，跳出循环，继续执行下一次
#         continue
#     print(i)
#         #break
#         # i= i+1
#
# print('end')

# print(abs(-12.1))#绝对值函数
# print(abs(20))
# print(max(4,6,8,1))
# print(int(12.0))
# print(int(-12))
#
# a=abs#变量a指向abs函数
# print(a(-12))
#
# n1=255
# n2=1000
# print(hex(n1))
# print(hex(n2))

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-99))
