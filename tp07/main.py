class A:
    
    def show( ):
        print('A',type(self))

class B(A):
    
    def show(self):
        print('B')

class C(A):
    
    def show(self):
        print('C')

class D(C,B):
    
    def show(self):
        print('D')
        super().show()
        super(C,self).show()
        super(B,self).show()


def main():
    obj = D()
    obj.show()
    print(D.mro())

if __name__=='__main__':
    main()
