
class Rectangle:
    
    
    def __init__(self,longueur,largeur):
        assert longueur >0
        assert largeur >0
        
        self.__longueur = longueur
        self.__largeur = largeur
        
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self,longueur):
        assert longueur >0
        self.__longueur = longueur

    def set_largeur(self,largeur):
        assert largeur >0 ,"largeur >0"       
        self.__largeur = largeur
        
    def get_surface(self):
        return self.__largeur * self.__longueur

    longueur = property(get_longueur,set_longueur,doc="la property longueur")
    largeur = property(get_largeur,set_largeur,doc="la property largeur")
    surface = property(get_surface,doc="la property surface")