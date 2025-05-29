# picaro.py
from sqlalchemy import Column, Integer
from entidades.upgrade import Upgrade
from random import randrange

class Picaro(Upgrade):
    # No definir __tablename__ aquí (ya está heredado de Upgrade)
    
    min_produccion = Column(Integer, default=0)  # Columna adicional para Picaro
    max_produccion = Column(Integer, default=0)  # Columna adicional para Picaro
    
    __mapper_args__ = {
        'polymorphic_identity': 'Picaro',
        'polymorphic_load': 'inline'
    }

    def __init__(self, nombre, coste, min_produccion, max_produccion,produccion_base, produccion, incPrecio):
        super().__init__(nombre, coste,produccion_base,produccion, incPrecio)
        self.min_produccion = min_produccion
        self.max_produccion = max_produccion

    def actualizarPrecio(self):
        new_cost = round((self.coste * 1) * self.incPrecio)
        self.coste = new_cost

    def calculo_produccion(self):
        min_prod = self.min_produccion if hasattr(self, 'min_produccion') else 3000
        max_prod = self.max_produccion if hasattr(self, 'max_produccion') else 35000
        
        try:
            return randrange(min_prod, max_prod)
        except Exception as e:
            print(f"Error calculating Picaro production: {e}")
            return 0