# aldeano.py
from sqlalchemy import Column, Integer
from entidades.upgrade import Upgrade

class Aldeano(Upgrade):
    
    __mapper_args__ = {
        'polymorphic_identity': 'aldeano',
    }
    
    def __init__(self, nombre, coste, produccion, efecto, incPrecio):
        super().__init__(nombre, coste,produccion, efecto, incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 0.9) * self.incPrecio)
        self.coste = new_cost