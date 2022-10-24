#raise 主动抛出异常
try:
    print("11")
    raise Exception("主动抛出异常")
    print("22")
except Exception as e:
    print("error",e)
