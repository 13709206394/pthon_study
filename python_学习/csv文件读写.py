import csv

# data = [["学号","姓名","性别","年龄","成绩"],
#         [1,"王祖贤","女",19,98],
#         [2,"刘诗诗","女",18,95],
#         [3,"赵露思","女",20,90],
#         [4,"唐  嫣","女",21,100]]
# with open(r"C:\Users\Test\Desktop\bbb.csv","w",newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#     print(writer)


with open(r"C:\Users\Test\Desktop\bbb.csv","r") as f:
    reader = csv.reader(f)
    data = []
    new_data = []
    for i in reader:
        data.append(i)
    print(data)
    print([j[1] for j in data])

    print(new_data.append())


# print(reader) #迭代器
