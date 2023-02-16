### 原型模式
import copy

class Book:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return str(sorted(self.__dict__.items()))

class ProtoType:
    def __init__(self):
        self.objects = dict()

    def register(self, nid, obj):
        self.objects[nid] = obj

    def unregister(self, nid):
        del self.objects[nid]

    def clone(self, nid, **attr):
        found = self.objects.get(nid)
        if not found:
            raise ValueError(f"{nid} No exist")
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

b_1 = Book("aaa", k="kkk", b="bbb")
prototype = ProtoType()
prototype.register("b_1", b_1)
b_2 = prototype.clone("b_1", e="eee", d="ddd")
print(b_1)
print(b_2)
print(id(b_1))
print(id(b_2))

