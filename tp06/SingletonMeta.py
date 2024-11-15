




class SingletonMeta(type):
    
    instance = None       # Attribut statique de classe

    def __call__(self,*args,**kwargs):
        if self.instance is None:
            self.instance = super().__call__(*args,**kwargs)
        else:
            self.instance.__init__(*args,**kwargs)
            
            
        return self.instance
