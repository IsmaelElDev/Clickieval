from sqlalchemy import Column, Integer
from entidades.upgrade import Upgrade

class Druida(Upgrade):
    
    __mapper_args__ = {
        'polymorphic_identity': 'Druida',
    }
    
    def __init__(self, nombre, coste, produccion_base,produccion, incPrecio):
        super().__init__(nombre, coste,produccion_base,produccion, incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 0.9) * self.incPrecio)
        self.coste = new_cost