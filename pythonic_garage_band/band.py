from abc import ABC, abstractmethod

class Musician:
    def __init__(self, name:str):
        self.name = name

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

class Guitarist(Musician):
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