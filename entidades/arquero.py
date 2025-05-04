# arquero.py
from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column
from entidades.upgrade import Upgrade

class Arquero(Upgrade):

    
    __mapper_args__ = {
        'polymorphic_identity': 'arquero',
    }
    
    def __init__(self, nombre, coste, produccion, efecto, incPrecio):
        super().__init__(nombre, coste,produccion, efecto, incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 1.01) * self.incPrecio)
        self.coste = new_cost