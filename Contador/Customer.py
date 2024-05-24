from abc import ABC
import Person
from faker import Faker
import Fakeable

class Customer(ABC,Fakeable):    
    def __init__(self,name,direction,phone):
        self.fake = Faker()
        self.name = name
        self.direction = direction
        self.phone = phone
        self.fillFake()
        
    def fillFake(self):        
        self.name = self.fake.name()
        self.direction = self.fake.address()
        self.telefono = self.fake.phone_number()           

class Domestic(Customer,Person):
    def __init__(self, name,direction,phone):
        Customer.__init__(name, direction,phone)
        Person.__init__(name, direction,phone)
        
        
class Industrial(Customer):
    def __init__(self, name,direction,phone,nif):
        Customer.__init__(name, direction,phone)
        self.cif = self.generar_cif()
        
