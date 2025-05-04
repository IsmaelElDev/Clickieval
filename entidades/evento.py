from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
import random
from pygame import time
from servicios.database import Base
from entidades.aldeano import Aldeano


class Evento(Base):
    __tablename__ = 'eventos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    probabilidad = Column(Float, nullable=False)
    duracion =  Column(Integer, nullable=True)
    enfriamiento = Column(Integer, nullable=False)
    tiempo_activacion = Column(Integer, nullable=True)
    partida_id = Column(Integer, ForeignKey('partidas.id'))
    
    def __init__(self,nombre,descripcion,probabilidad,duracion,enfriamiento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.probabilidad = probabilidad
        self.duracion = duracion
        self.enfriamiento = enfriamiento
        self.tiempo_activacion = None
        self.activo = False


    def efectoEvento(self,partida):
        if self.nombre == 'Guerra':
            aldeanos = [mejora for mejora in partida.mejoras if isinstance(mejora, Aldeano)]
            # Obtener los últimos 5
            aldeanos_a_borrar = aldeanos[-5:]

            # Eliminar esos objetos de la lista completa
            for aldeano in aldeanos_a_borrar:
                partida.mejoras.remove(aldeano)

        elif self.nombre == 'Despertar Ruinas' and not self.activo:
            partida.oro_por_click *= 10
            self.tiempo_activacion = time.get_ticks()
            self.activo = True  # <--- MARCAR COMO ACTIVO

    def sucedeEvento(self):
        num = random.random()
        if not num > self.probabilidad and not num < 0:
            return True
        
        return False
    
    def desactivarEvento(self, partida):
        
        if self.nombre == 'Despertar Ruinas':
            partida.oro_por_click = int(partida.oro_por_click / 10)

    def verificarDuracion(self, partida, tiempo_actual):
        if self.duracion is not None and self.activo:
            tiempo_transcurrido = (tiempo_actual - self.tiempo_activacion) / 1000
            if tiempo_transcurrido >= self.duracion:
                self.desactivarEvento(partida)
                self.activo = False  # <--- IMPORTANTE
                return True
            
        return False
    
    def nuevaInstancia(self):
        new_nombre = self.nombre 
        new_descripcion = self.descripcion 
        new_probabilidad = self.probabilidad 
        new_duracion = self.duracion 
        new_enfriamiento = self.enfriamiento
        new_tiempo_activacion = self.tiempo_activacion
        new_activo = self.activo 

        new_evento = Evento(new_nombre,new_descripcion,new_probabilidad,new_duracion,new_enfriamiento)
        return new_evento
