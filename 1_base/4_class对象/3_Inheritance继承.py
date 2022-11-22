class Animal(object):
    def run(self):
        print("Animal running ...")

#类的特性，继承
class dog(Animal):
    pass

class cat(Animal):
    pass

dog_a = dog()
cat_a = cat()
dog_a.run()
cat_a.run()