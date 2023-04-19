from struct import *

# int 转 bytes
a=10
b=pack("i",a)
print("int 转 bytes:",b)

# float 转 bytes
a=3.14
b=pack("f",a)
print("float 转 bytes:",b)

# char 转 bytes
a='a'   # 错误
a=b'a'
b=pack("c",a)
print("char 转 bytes:",b)

# unsigned char 转 bytes
a=254
b=pack("B",a)
print("unsigned char 转 bytes:",b)

# 数组 转 bytes
a=[1,2,3,4]
b=pack("4B",*a)
print("数组 转 bytes:",b)

#