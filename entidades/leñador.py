# lenyador.py
from sqlalchemy import Integer,Column
from sqlalchemy.orm import mapped_column, column_property
from entidades.upgrade import Upgrade

class Lenyador(Upgrade):

    __mapper_args__ = {
        'polymorphic_identity': 'lenyador',
    }
    
    def __init__(self, nombre, coste, produccion, efecto, incPrecio):
        super().__init__(nombre, coste,produccion, efecto, incPrecio)

    def actualizarPrecio(self):
        new_cost = round((self.coste * 0.98) * self.incPrecio)
        self.coste = new_cost