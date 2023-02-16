class A:
    def m(self):
        print('A')
 
class B:
    def m(self):
        print('B')
 
class C(B):
    def m(self):
        print('C')
        # super().m()
        super(C,self).m()
 
C().m()