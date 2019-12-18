from types import MethodType
class Student(object):
    pass
def set_age(self,age):#定义一个函数作为实例方法
    self.age=age
# s=Student()#创建实例
# s.set_age = MethodType(set_age,s)#给实例绑定一个方法
# s.set_age(25)#尝试调用方法
# print(s.age)

def set_score(self,score):
    self.score=score
Student.set_score=set_score#给实例变量赋值

s=Student()#创建实例
s.set_score(100)
s1=Student()
s1.set_score(25)
print(s.score)
print(s1.score)

class Dog(object):
    __slots__ = ('name','age')#用tuple定义允许绑定的属性名称
#在定义class的时候，定义一个特殊的__slots__变量，来限制class实例能添加的属性
class Black_Dog(Dog):
    pass

d=Dog()
d.name='lacy'
d.age=3
d.coller='red'
print(d.name)
print(d.age)
print(d.coller)

b=Black_Dog()
b.score=999
print(b.score)
#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的；
#除非在子类中也定义__slots__,这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__



