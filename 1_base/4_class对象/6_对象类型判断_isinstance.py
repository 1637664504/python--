class Animal(object):
    def run(self):
        print("Animal running ...")

class dog(Animal):
    #多态
    def run(self):
        print("Dog running +++")

class cat(Animal):
    #多态
    def run(self):
        print("Cat running ***")

dog_a = dog()
dog_b = dog()
cat_a = cat()
list_a = list()
animal_a = Animal()

ret = isinstance(list_a,list)
ret = isinstance(dog_a,dog)
ret = isinstance(animal_a,dog)
# ret = isinstance(dog_a,dog_b)   #error: isinstance() arg 2 must be a type or tuple of types

print("end -----")