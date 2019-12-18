def fn(self,name="world"):
    print('Hello,%s.'%name)
Hello=type('Hello',(object,),dict(hello=fn))#创建Hello class
h=Hello()
h.hello()
