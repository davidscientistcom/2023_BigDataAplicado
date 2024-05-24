from abc import abstractmethod

class Fakeable:
    @abstractmethod
    def fillFake(self):
        pass
    
    def generar_id(self):        
        base = self.fake.random_number(digits=8, fix_len=True)   
        inicio = self.fake.random_element(elements=('A','B','C','D','E','F','G','H','J','U','V'))   
        letras_control = "JABCDEFGHI"
        suma = sum((2 if i % 2 else 1) * int(n) for i, n in enumerate(str(base)))
        modulo = suma % 10
        digito_control = 10 - modulo if modulo else 0
        letra_control = letras_control[digito_control]
        
        return f"{inicio}{base}{letra_control}"