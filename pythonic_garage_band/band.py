
from abc import ABC
class Musician(ABC):
    def __init__(self,name):
        self.name=name

class Guitarist(Musician):
    def __str__(self):
        return (f"My name is {self.name} and I play guitar")
    
    def __repr__(self):
        return (f"{__class__.__name__} instance. Name = {self.name}")


class Drummer(Musician):
     def __str__(self):
        return (f"My name is {self.name} and I play drums")
    
     def __repr__(self):
        return (f"{__class__.__name__} instance. Name = {self.name}")


class Bassist(Musician):
    def __str__(self):
        return (f"My name is {self.name} and I play bass")
    
    def __repr__(self):
        return (f"{__class__.__name__} instance. Name = {self.name}")
