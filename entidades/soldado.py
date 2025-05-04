from sqlalchemy import Column, Integer
from entidades.upgrade import Upgrade

class Soldado(Upgrade):
    
    __mapper_args__ = {
        'polymorphic_identity': 'soldado',
    }
    
    def __init__(self, nombre, coste, produccion, efecto, incPrecio):
        super().__init__(nombre, coste,produccion, efecto, incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 1.2) * self.incPrecio)
        self.coste = new_cost