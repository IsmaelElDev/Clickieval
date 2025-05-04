# mago.py
from sqlalchemy import Column, Integer
from entidades.upgrade import Upgrade

class Mago(Upgrade):
    
    __mapper_args__ = {
        'polymorphic_identity': 'mago',
    }
    
    def __init__(self, nombre, coste, produccion, efecto, incPrecio):
        super().__init__(nombre, coste,produccion, efecto, incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 1.10) * self.incPrecio)
        self.coste = new_cost