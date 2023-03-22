class Foo(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

a = Foo()
b = Foo()
print(id(a)==id(b))

# 得到 True