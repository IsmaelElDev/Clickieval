# mago.py
from sqlalchemy import Column, Integer
from entidades.upgrade import Upgrade

class Mago(Upgrade):
    
    __mapper_args__ = {
        'polymorphic_identity': 'Mago',
    }
    
    def __init__(self, nombre, coste, produccion_base,produccion, incPrecio):
        super().__init__(nombre, coste,produccion_base,produccion, incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 1.10) * self.incPrecio)
        self.coste = new_cost