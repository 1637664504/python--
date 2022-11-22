class student(object):
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.__height = height
    def show_info(self):
        print("name=%s age=%d" % (self.name,self.age))

lili=student("lili",18,170)
lili.show_info()
lili.__height   #提示错误 'student' object has no attribute '__height'
