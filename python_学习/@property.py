# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an install!')
#         if value<0 or value>100:
#             raise ValueError('score must be between 0~100!')
#         self._score=value
# s=Student()
# s.set_score(60)
# print(s.get_score())#print(s._score)

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# @property装饰器就是负责把一个方法变成属性调用的
class Screen(object):
    @property
    def width(self):
        # return self._width
        pass
    @width.setter
    def width(self,width):
        self._width=width

    @property
    def height(self):
        pass
        # return self._height
    @height.setter
    def height(self,height):
        self._height=height

    @property
    def resolution(self):
        return self._height*self._width


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')