class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Woman(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        # super().__init__()
        print("init woman ",name)

class Man(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        # super().__init__()
        print("init man ",name)

class PersonFactory():
    # @staticmethod
    def getPersonImpl(manType,name,age):
        if manType == 'man':
            return Man(name,age)
        elif manType == 'woman':
            return Woman(name,age)

        raise Exception("未知 person 类型")

lili = Woman('lili',15)
Mark = Man('Mark',16)
print(lili.name)
print(Mark.name)

Ailisi = PersonFactory.getPersonImpl('woman','Ailisi','16')
print(Ailisi.name)

# Malike = PersonFactory.getPersonImpl('god','Malike','16')
# print(Malike.name)
