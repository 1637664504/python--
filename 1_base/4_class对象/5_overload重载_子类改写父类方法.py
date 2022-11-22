class Animal(object):
    def run(self):
        print("Animal running ...")
    def run_twice(self):
        self.run()
        print("run twice..")

class dog(Animal):
    #重载
    def run(self):
        print("Dog running +++")

class cat(Animal):
    #重载
    def run(self):
        print("Cat running ***")

dog_a = dog()
cat_a = cat()
dog_a.run_twice()
cat_a.run_twice()


''' 和c++一样:
    1.子类重载父类
    2.虚函数

result:
Dog running +++
run twice..
Cat running ***
run twice.. 
'''
