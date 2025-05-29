# partida.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from servicios.database import Base


class Partida(Base):
    __tablename__ = 'partidas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    oro = Column(Integer, default=0)
    oro_por_segundo = Column(Integer, default=0)
    oro_por_click = Column(Integer, default=5)
    oro_total = Column(Integer, default=0)
    oro_gastado = Column(Integer, default=0)
    madera = Column(Integer, default=0)
    madera_por_segundo = Column(Integer, default=0)
    madera_por_click = Column(Integer, default=5)
    madera_total = Column(Integer, default=0)
    madera_gastada = Column(Integer, default=0)
    magia = Column(Integer, default=0)
    magia_por_segundo = Column(Integer, default=0)
    magia_total = Column(Integer, default=0)
    magia_gastada= Column(Integer, default=0)
    pantalla_estadisticas = Column(Boolean, default=False)
    pantalla_refrescar = Column(Boolean, default=False)
    # Define la relación
    mejoras = relationship("Upgrade", backref="partida_obj",lazy='joined')
    eventos = relationship("Evento", backref="evento_obj")

    def __init__(self,nombre="Partidas"):
        self.nombre = nombre
        self.oro = 0
        self.oro_por_segundo = 0
        self.oro_por_click = 1
        self.oro_total = 0
        self.oro_gastado = 0
        self.madera = 0
        self.madera_por_segundo = 0
        self.madera_por_click = 1
        self.madera_total = 0
        self.madera_gastada = 0
        self.magia = 0
        self.magia_por_segundo = 0
        self.magia_total = 0
        self.magia_gastada = 0
        self.pantalla_estadisticas = False
        self.pantalla_refrescar = False