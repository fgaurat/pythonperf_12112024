


class Test:
    
    def __new__(cls):
        print("def __new__(cls)")
        return object.__new__(cls)
    
    def __init__(self):
        print("def __init__(self)")
        self.p = "toto"
        
    def __call__(self):
        print("def __call__(self)")