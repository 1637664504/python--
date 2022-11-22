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
cat_a = cat()
dog_a.run()
cat_a.run()