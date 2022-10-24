#try..else 如未捕获到异常，那么就执行else中的事情
try:
    print("11")
    #raise Exception("主动抛出异常")
    print("22")
except Exception as e:
    print("error",e)
else:
    print("333")
