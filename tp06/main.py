from RectangleSingleton import RectangleSingleton
from RectangleSingletonMeta import RectangleSingletonMeta
from RectangleSingletonDeco import RectangleSingletonDeco
from Test import Test
def main():
    r = RectangleSingleton(2,3)
    print(type(r))
    print(type(RectangleSingleton))
    t = Test()
    
    t() 
    
    r = RectangleSingleton(2,3)
    print(hex(id(r)))
    print(r)
    r1 = RectangleSingleton(15,93)
    print(hex(id(r1)))
    print(r1)
    
    r1.longueur =1000
    print(r1)
    print(r)
    print(50*'-')
    r2 = RectangleSingletonMeta(2,3)
    r3 = RectangleSingletonMeta(25,63)
    print(type(RectangleSingletonMeta))
    print(hex(id(r2)))
    print(hex(id(r3)))
    print(r2)
    print(r3)
    print(50*'-')
    r2 = RectangleSingletonDeco(2,3)
    r3 = RectangleSingletonDeco(2,3)
    print(hex(id(r2)))
    print(hex(id(r3)))
    print(r2)
    print(r3)
    
if __name__=='__main__':
    main()
