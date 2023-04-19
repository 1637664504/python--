# 将bytes打印为hex
a=b'123456789abcdefghijklmnopqrstuvwxyz'
def show_hex(val):
    cnt = 0
    for i in val:
        print("%2x"%(i),end=' ')
        cnt+=1
        if cnt%16 == 0:
            print('--')

show_hex(a)

''' 
31 32 33 34 35 36 37 38 39 61 62 63 64 65 66 67 --
68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 --
78 79 7a
'''