# from enum import Enum
# Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# # print(type(Month))
# # 可以直接使用Month.Jan来引用一个常亮，或者枚举它的所以成员：
# for name,member in Month.__members__.items():
#     print(name,'=>',member,',',member.value)#value属性则是自动赋给成员的int常亮，默认从1开始计数。
#

# 如果需要更经精确的控制枚举类型，可以从Enum派生出自定义类
from enum import Enum,unique
#
# 若要不能定义相同的成员值，可以通过 unique 装饰
# @unique
# class Weekday(Enum):
#     Sun = 0#Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# day1=Weekday.Mon
# day2=Weekday.Sun
# print(day1,day2)
# print(Weekday['Tue'])
# print(Weekday.Sun.value)
# print(Weekday(1))
#
# for name,member in Weekday.__members__.items():
#     print(name,'=>',member)


# 把Student的gender属性改造为枚举类型，可以避免使用字符串
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if isinstance(gender,Gender):
            self.gender = gender
        else:
            print('gender must be Gender type')

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')