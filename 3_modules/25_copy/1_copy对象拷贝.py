import copy

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

lili = person('lili',15)
keni = person('keni',16)

# lili_copy = lili.copy
lili_copy = copy.copy(lili)
lili_copy.name='lili_bak'

print(lili)
print(lili_copy)