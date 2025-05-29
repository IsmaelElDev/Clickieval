# arquero.py
from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column
from entidades.upgrade import Upgrade

class Arquero(Upgrade):

    
    __mapper_args__ = {
        'polymorphic_identity': 'Arquero',
    }
    
    def __init__(self, nombre, coste, produccion_base,produccion, incPrecio):
        super().__init__(nombre, coste,produccion_base,produccion, incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 1.01) * self.incPrecio)
        self.coste = new_cost