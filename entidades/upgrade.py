# upgrade.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from servicios.database import Base

class Upgrade(Base):
    __tablename__ = 'mejoras'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    coste = Column(Integer, nullable=False)
    efecto = Column(String)
    incPrecio = Column("inc_precio", Float, nullable=False)  # Mapeo directo del nombre Python al de la BD
    tipo = Column(String)
    produccion = Column(Integer, default=0)
    
    partida_id = Column(Integer, ForeignKey('partidas.id'))
    
    __mapper_args__ = {
        'polymorphic_identity': 'upgrade',
        'polymorphic_on': tipo
    }

    def __init__(self, nombre, coste,produccion, efecto, incPrecio):
        self.nombre = nombre
        self.produccion = produccion
        self.coste = coste
        self.efecto = efecto
        self.incPrecio = incPrecio

    def actualizarPrecio(self):
        new_cost = round((self.coste * 0.9) * self.incPrecio)
        self.coste = new_cost