
import struct
a:float = 3.14

# float 转 bytes
b= struct.pack("f",a)
print(len(b),b)

# bytes 转 float
c = struct.unpack("f",b)[0]
print(len(c),c)


# 运行错误
# d = float(b)
# print(len(d),d)