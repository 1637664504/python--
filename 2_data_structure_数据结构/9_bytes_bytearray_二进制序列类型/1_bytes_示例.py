a = bytes.fromhex('1f2f 4f11')
print(a)
print(a.hex())

b= bytes.fromhex('12345678abcd')
print(b.hex(' ',1))