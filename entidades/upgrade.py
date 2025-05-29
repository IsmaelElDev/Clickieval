# upgrade.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from servicios.database import Base

class Upgrade(Base):
    __tablename__ = 'mejoras'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    coste = Column(Integer, nullable=False)
    incPrecio = Column("inc_precio", Float, nullable=False)  # Mapeo directo del nombre Python al de la BD
    produccion = Column(Integer, default=0)
    produccion_base = Column(Integer, default=0)
    
    partida_id = Column(Integer, ForeignKey('partidas.id'))
    
    __mapper_args__ = {
        'polymorphic_identity': 'upgrade',
        'polymorphic_on': nombre
    }

    def __init__(self, nombre, coste,produccion_base,produccion, incPrecio):
        self.nombre = nombre
        self.produccion_base = produccion_base
        self.produccion = produccion
        self.coste = coste
        self.incPrecio = incPrecio
        self.locked = True

    def actualizarPrecio(self):
        new_cost = round((self.coste * 0.9) * self.incPrecio)
        self.coste = new_cost