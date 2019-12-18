import functools

int2=functools.partial(int,base=10)
print(int2('1010'))
max2 = functools.partial(max,10)
print(max2(2,5,7,20))