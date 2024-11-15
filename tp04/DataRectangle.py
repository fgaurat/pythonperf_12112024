from dataclasses import dataclass
from typing import ClassVar

@dataclass(slots=True)
class DataRectangle:

    longueur:int=0
    largeur:int=0
    counter: ClassVar[int] = 0 

    def __post_init__(self):
       DataRectangle.counter+=1