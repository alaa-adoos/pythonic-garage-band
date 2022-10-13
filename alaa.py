from abc import ABC

class Musician(ABC): 
    alaa="alaa"
    def __init__(self,list1):
        self.list1=[]
    
class Guitarist(Musician):
    def __init__(self,name):
        
        self.name=name
    def __str__(self):
        return (f"My name is {self.name} and I play guitar")
    
    def __repr__(self):
        return (f"{__class__.__name__} instance. Name = {self.name}")

    def get_var(self):
        return self.alaa
obj=Guitarist("alaa")
print(obj.get_var())