class Animal():
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        pass

    def set_name(self):
        pass

class Mammal(Animal):
    def __init__(self, name, no_legs, has_fur):
        super().__init__(name)
        self.no_legs = no_legs
        self.has_fur = has_fur

    def get_no_legs(self):
        pass

    def set_no_legs(self):
        pass

    def get_has_fur(self):
        pass

    def set_has_fur(self):
        pass

class Canine(Mammal):
    def __init__(self, name, no_legs, has_fur, howl, bark):
        super().__init__(name, no_legs, has_fur)
        self.howl = howl
        self.bark = bark

class Dog(Canine):
    def __init__(self, name, no_legs, has_fur, howl, bark, kind, owner):
        super().__init__(name, no_legs, has_fur, howl, bark)
        self.kind = kind
        self.owner = owner

    def get_kind(self):
        pass

    def set_kind(self):
        pass

    def get_owner(self):
        pass

    def set_owner(self):
        pass

animal1 = Animal('Monke')
animal1.get_name()
animal1.set_name()

#nie wyrobiłem się, żeby rozpisać