# 可迭代对象：就是使用for循环遍历取值的对象就是可迭代对象
# for循环可以直接遍历取值的对象: 列表，元组，字典，字符串，集合，range

# for value in ["1", "2"]:
#     print(value)

from collections import Iterable
# 判断对象是否是指定类型
result = isinstance([1, 2], Iterable)

print(result)

result = isinstance((1, 2), Iterable)

print(result)

result = isinstance({"name": "李四"}, Iterable)

print(result)

result = isinstance("李四", Iterable)

print(result)

result = isinstance({"李四", "王五"}, Iterable)

print(result)

result = isinstance(range(10), Iterable)

print(result)

# 可迭代对象有一个__iter__方法

result = dir([1, 2])
print(result)

# 提示： 数字不是可迭代类型，数字是int类型
# 提示： isinstance可以判断参数的类型是否是你想要的类型
result = isinstance(10, int)

print(result)