import struct

a: float = 3.14
b: float = 2.18
c: int = 0x2
d: int = 0x0fff

b_str = struct.pack("ffBI",a,b,c,d)
print(b_str)

e,f,g,h = struct.unpack("ffBI",b_str)
print(e,f,g,h)