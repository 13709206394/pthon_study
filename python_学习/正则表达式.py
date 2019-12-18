# ls = [1, 2, 3, 4, 4, 5, 6, 67]
# # print(ls[::-1])
# # ls.reverse()  # reverse()是Python列表内置的一个方法（字典、字符串、元组是没有的），该方法用于列表中比数据的反转
# # print(ls)
# f = reversed(ls)
# print(list(f))
#
# ss = "qwer1234"
# print(''.join(reversed(ss)))

# def BinarySearch(arr, key):
#     min = 0
#     max = len(arr) - 1
#     if key in arr:
#         while max>0:
#             center = int((min + max) / 2)
#             if key>center:
#                 max = center - 1
#             elif key<center:
#                 min = center + 1
#             else:
#                 return arr[center]
#     else:
#         return -1
# print(BinarySearch([1,2,3,4,5,6],2))
#
# str = "jskdrfiweurb"
# print(str[::-1])
#
# new_str = ''.join(reversed(str))
# print(new_str)

# str = "a"
# print(id(str))
# str = "b"
# print(id(str))

# list = []
# print(id(list))
#
# list = [2]
# print(id(list))

# tuple = (1,2,3,4)
# # print(id(tuple[0]))  # 元素地址不变
# tuple = (1,2,3,4,5)
# # print(id(tuple[0]))
# tuple = (1,2,3,4,5,[1])
# # print(id(tuple[0]))
# print(id([5]))
# tuple = (1,2,3,4,5,[1,2])
# # print(id(tuple[0]))
# print(id([5]))
# tuple = (1,2,3,4,5,[1,2,3])
# # print(id(tuple[0]))
# print(id([5]))


