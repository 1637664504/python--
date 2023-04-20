from crc import Calculator,Crc16

crc16_fun=Calculator(Crc16.CCITT,optimized=True)
data = "123456".encode()
result = crc16_fun.checksum(data)
print(data)
print(hex(result))