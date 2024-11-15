from Rectangle import Rectangle
from DataRectangle import DataRectangle
import inspect
from pprint import pprint
def main():
    r = Rectangle(2,3)
    # print(r.get_longueur())
    # print(r.get_largeur())
    # print(r.get_surface())
    # r.set_largeur(-10)
    # print(r.get_largeur())
    # print(r.get_surface())
    print(r.longueur)
    r.longueur = 12
    print(r.surface)
    
    s = str(r)
    print(s)
    print(50*'-')
    r = Rectangle(2,3)
    r1 = Rectangle(2,3)
    if r==r1:
        print("ok")
    else:
        print("ko")
    
    print(r.get_cpt())        
    del r
    print(Rectangle.get_cpt())
    print(50*'-')
    line = '5;3'

    r = Rectangle.build_from_str(line)
    print(r)
    print(50*'-')
    dr = DataRectangle(2,6)
    dr1 = DataRectangle(2,6)
    print(dr)
    # dr.toto="truc"
    if dr == dr1:
        print("ok") 
    print(DataRectangle.counter)   
    print(50*'-')
    r = Rectangle(5,6)
    # r.toto="truc"
    # print(r)
    # print(r.__dict__)
    pprint(inspect.getmembers(r))
if __name__=='__main__':
    main()
