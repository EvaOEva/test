# 引用：通俗理解就是程序中的数据在内存中的地址，简称内存地址

a = 10 # a存储的是10在内存中的一个地址，数据10的内存地址

b = a # b存储的是a保持的内存地址，现在a和b存储的内存地址是同一个，以后可以通过内存地址获取对应的数据

# id(变量名)获取的内存地址是一个十进制的数据
print("a保存的数据的内存地址: ", id(a))
print("b保存的数据的内存地址: ", id(b))

print("a保存的数据的内存地址: ", hex(id(a)))
print("b保存的数据的内存地址: ", hex(id(b)))

print(a, b)

a = 20
print("a保存的数据的内存地址: ", id(a))
print("b保存的数据的内存地址: ", id(b))

print("a保存的数据的内存地址: ", hex(id(a)))
print("b保存的数据的内存地址: ", hex(id(b)))


