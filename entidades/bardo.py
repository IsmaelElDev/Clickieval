from sqlalchemy import Column, Integer
from entidades.upgrade import Upgrade

class Bardo(Upgrade):
    
    __mapper_args__ = {
        'polymorphic_identity': 'bardo',
    }
    
    def __init__(self, nombre, coste, produccion, efecto, incPrecio):
        super().__init__(nombre, coste,produccion, efecto, incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 1.1) * self.incPrecio)
        self.coste = new_cost