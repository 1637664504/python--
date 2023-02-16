''' 
只能有一个对象存在
'''
class demo():
    def __new__(cls, *args, **kwargs):
        print("111")
        if not hasattr(cls,'_instance'):
            cls._instance = cls.__init__(cls)
        return cls._instance

    def __init__(self,explain='none'):
        print("222")
        print(explain)


obj1=demo('11')
obj2=demo('22')
print(id(obj1),id(obj2))