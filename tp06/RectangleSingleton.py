
class RectangleSingleton:
    __cpt=0
    __slots__ = '__longueur','__largeur'
    
    instance = None       # Attribut statique de classe
    def __new__(cls,*args,**kwargs): 
        "méthode de construction standard en Python"
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance
    

    
    def __init__(self,longueur=1,largeur=1):
        assert longueur >0
        assert largeur >0
        
        self.__longueur = longueur
        self.__largeur = largeur
        
        RectangleSingleton.__cpt+=1
    
    @classmethod
    def build_from_str(cls,value):
        values = [int(i) for i in value.split(';')] 
        return cls(*values)
    
    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @longueur.setter
    def longueur(self,longueur):
        assert longueur >0
        self.__longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        assert largeur >0 ,"largeur >0"       
        self.__largeur = largeur
    
    @property 
    def surface(self):
        return self.__largeur * self.__longueur
    
    @staticmethod
    def get_cpt():
        return RectangleSingleton.__cpt
        
    def __str__(self):
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"
    
    # r == r1 = r.__eq__(r1)
    def __eq__(self,obj):
        return self.__largeur == obj.__largeur and self.__longueur == obj.__longueur 
        
    def __del__(self):
        RectangleSingleton.__cpt -=1