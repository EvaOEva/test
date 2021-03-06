# 字典: 以大括号表现形式的键值对数据的集合， 比如: {'name': '张三', 'age': 18}
# 提示： key一般都是字符串(99%)，key只能是不可变类型：数字，字符串，元组， 不能使用可变类型：[],{}
my_dict = {'name': '张三', 'age': 18}

print(my_dict, type(my_dict))

# 通过key获取对于的value值， key值在字典里面是唯一的
value = my_dict["name"]

print(value)

# 设置默认值
result = my_dict.get("name", "男")

print(result)

# my_dict["sex"] , my_dict.get("sex") , 中括号方式取值如果key不存在那么会崩溃， get方式取值不会， 取值不成功返回None

