# lenyador.py
from sqlalchemy import Integer,Column
from sqlalchemy.orm import mapped_column, column_property
from entidades.upgrade import Upgrade

class Lenyador(Upgrade):

    __mapper_args__ = {
        'polymorphic_identity': 'Lenyador',
    }
    
    def __init__(self, nombre, coste, produccion_base,produccion, incPrecio):
        super().__init__(nombre, coste,produccion_base,produccion, incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 0.98) * self.incPrecio)
        self.coste = new_cost