from Carre import Carre
from Cercle import Cercle
from ICalcGeo import ICalcGeo
from typing import Protocol

class SurfaceAble(Protocol):
    
    @property
    def surface(self):
        pass

def show_surface_protocol(o:SurfaceAble):
    print(o.surface)
    print(type(o))
    
    
def show_surface(o:ICalcGeo):
    print(o.surface)
    print(type(o))
    
    
def main():
    c = Carre(2)
    print(c.surface) # 4
    print(c.cote)
    print(c)
    c.cote = 5
    print(c.surface) # 25
    ce = Cercle(2)
    
    print(ce.surface)
    show_surface(c)
    show_surface(ce)
    print(50*'-')
    show_surface_protocol(c)
    show_surface_protocol(ce)
if __name__=='__main__':
    main()
