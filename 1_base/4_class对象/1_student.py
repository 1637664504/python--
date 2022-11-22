class student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_info(self):
        print("name=%s age=%d" % (self.name,self.age))

lili=student("lili",18)
lili.show_info()
