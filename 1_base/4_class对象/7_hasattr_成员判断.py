''' 
bool hasattr(class, object)
返回  hasattr(类, 对象)
'''

class student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

lili = student('lili',15)
if hasattr(lili,'name'):
    print("has name")

if hasattr(lili,'weight'):
    print("has weight")

# Result
''' 
has name
'''