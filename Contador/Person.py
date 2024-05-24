from abc import ABC
from faker import Faker
import Fakeable
import Person    

class Person(ABC,Fakeable):
    def __init__(self,name,direction,phone):
        self.fake = Faker()
        self.name = name
        self.direction = direction
        self.phone = phone
        self.dni = self.generar_id()
        self.fillFake()
    
    def fillFake(self):        
        self.name = self.fake.name()
        self.direction = self.fake.address()
        self.telefono = self.fake.phone_number()

        
        
class Worker(Person):
    def __init__(self, name,direction,phone):
        super().__init__(name, direction, phone)
        




         

