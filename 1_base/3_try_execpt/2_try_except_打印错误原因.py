#打印错误 异常原因
try:
    print("11")
    2/0
    print("22")
except Exception as e:
    print("error",e)

print("end---")