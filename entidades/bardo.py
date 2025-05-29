from sqlalchemy import Column, Integer
from entidades.upgrade import Upgrade

class Bardo(Upgrade):
    
    __mapper_args__ = {
        'polymorphic_identity': 'Bardo',
    }
    
    def __init__(self, nombre, coste, produccion_base,produccion, incPrecio):
        super().__init__(nombre, coste,produccion_base,produccion,incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 1.1) * self.incPrecio)
        self.coste = new_cost