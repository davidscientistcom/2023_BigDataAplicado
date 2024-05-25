from faker import Faker
from enum import Enum

class TypeEntity(Enum):
    URBAN_LOW = 1
    URBAN_MEDIUM = 2
    URBAN_HIGHT = 3
    INDUSTRIAL_LOW = 4
    INDUSTRIAL_MEDIUM = 5
    INDUSTRIAL_HIGHT = 6
    WORKER = 7
    

class Entity():
    def __init__(self,name,direction,phone,typeEntity):
        super().__init__()
        self.fake = Faker()
        self.name = name
        self.direction = direction
        self.phone = phone        
        self.type = typeEntity
        self.fillFake()
    
    def fillFake(self):        
        self.name = self.fake.name()
        self.direction = self.fake.address()
        self.telefono = self.fake.phone_number()
        self.dni = self.generate_id()
    
    
    def generate_id(self):        
        base = self.fake.random_number(digits=8, fix_len=True)   
        letras_control = "ABCDEFGHIJKLMNOPQRTUVWXYZ"
        suma = sum((2 if i % 2 else 1) * int(n) for i, n in enumerate(str(base)))
        modulo = suma % 10
        digito_control = 10 - modulo if modulo else 0
        letra_control = letras_control[digito_control]
        
        return f"{base}{letra_control}"    
    
    
    def _show(self):
        for atributo, valor in self.__dict__.items():
            print(f"{atributo} -> {valor}")
            
            
    @classmethod
    def get_n(cls, nombre_base,type_entity,n):
        return [cls(f"{nombre_base} {i}",type_entity) for i in range(1, n+1)]

class FakeEntity(Entity):
    def __init__(self,type):
        fake = Faker()
      
        name = fake.name()
        direction = fake.address()
        phone = fake.phone_number()
        self.type = type
        typeEntity = fake.random_element(elements=TypeEntity)        
        super().__init__(name, direction, phone, typeEntity)
    
    @classmethod
    def get_n(cls, nombre_base,type_entity,n):
        return [cls(type_entity) for i in range(1, n+1)]
    




         

