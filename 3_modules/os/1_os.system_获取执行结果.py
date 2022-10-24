import os
cmd = "ping www.qq.com -w8 -c2"
ret = os.system(cmd)
print("ping reuslt ",ret)