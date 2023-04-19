import struct

a=10
b=20
c=3.14
d=1.11
f=struct.pack("iiff", a, b, c, d)
print(f)

# 解析源数据
A,B,C,D = struct.unpack("iiff", f)
print(A, B, C, D)
''' result:
10 20 3.140000104904175 1.1100000143051147
'''

# 解析int
data=struct.pack("i", a)
b_a = struct.unpack("i",data)[0]
print("bytes解析int",b_a)

# 解析float
data=struct.pack("f", c)
b_c = struct.unpack("f",data)[0]
print("bytes解析float",b_c)

# 解析char
src = '1'
data=struct.pack("c", src.encode())
dst = struct.unpack("c",data)[0].decode()
print("bytes解析char",dst)
