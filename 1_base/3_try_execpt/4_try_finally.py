#
#如果一个段代码必须要执行，即无论异常是否产生都要执行，那么此时就需要使用finally。 
#比如文件关闭，释放锁，把数据库连接返还给连接池等。
try:
    print("11")
    raise Exception("主动抛出异常")
    print("22")
except Exception as e:
    print("error",e)
finally:
    print("333")