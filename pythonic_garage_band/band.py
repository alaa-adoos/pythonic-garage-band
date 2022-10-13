from abc import ABC, abstractmethod

class Musician:
    '''
    base class (parent)
    contain __str__,__repr__ function that return a name and instrument for the Musician
    and there is a  get_instrument method that return the what every Musician play with
    And in the end we have play_solo method that a abstract method 
    
    '''
    def __init__(self, name:str):
        self.name = name

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

class Guitarist(Musician):
    '''
    sub class (child)
    it inherits attributes and method from the base class (Musician)
    and there is a play_solo method that return what the Musician plays
    
    '''
    def __init__(self, name:str):
        self.name=name
   

    def __str__(self):
        return (f"My name is {self.name} and I play guitar")

    def __repr__(self):
        return (f"Guitarist instance. Name = {self.name}")

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    '''
    sub class (child)
    it inherits attributes and method from the base class (Musician)
    and there is a play_solo method that return what the Musician plays
    
    '''
    def __init__(self, name:str):
        super().__init__(name)

    def __str__(self):
        return (f"My name is {self.name} and I play bass")

    def __repr__(self):
        return (f"Bassist instance. Name = {self.name}")

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    '''
    sub class (child)
    it inherits attributes and method from the base class (Musician)
    and there is a play_solo method that return what the Musician plays
    
    '''

    def __init__(self, name:str):
        super().__init__(name)

    def __str__(self):
        return (f"My name is {self.name} and I play drums")

    def __repr__(self):
        return (f"Drummer instance. Name = {self.name}")

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

class Band:
    '''
    sub class (child)
    it inherits attributes and method from the base class (Musician)
    also it have a to_list method that a class method 
    and there is a play_solos method that contain a for loop to represent what each member plays
    
    '''
    instances = []
    def __init__(self, name:str, members:list):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        to_return = []
        for i in self.members:
            to_return.append(i.play_solo())
        return to_return

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @classmethod
    def to_list(cls):
        return Band.instances