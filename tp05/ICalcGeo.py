from abc import ABC,abstractmethod


class ICalcGeo(metaclass=ABCMeta):
    
    @property
    @abstractmethod
    def surface(self):
        pass