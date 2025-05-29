from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
import random
from pygame import time
from servicios.database import Base
from entidades.aldeano import Aldeano
from entidades.leñador import Lenyador
from entidades.arquero import Arquero
from entidades.picaro import Picaro
from entidades.mago import Mago
from entidades.bardo import Bardo
from entidades.soldado import Soldado
from entidades.clerigo import Clerigo
from entidades.druida import Druida
from entidades.bruja import Bruja
from entidades.noble import Noble
from utils.actualizarProducciones import actualizar_producciones


class Evento(Base):
    __tablename__ = 'eventos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(Integer, nullable=False)
    probabilidad = Column(Float, nullable=False)
    duracion =  Column(Integer, nullable=True)
    enfriamiento = Column(Integer, nullable=False)
    tiempo_activacion = Column(Integer, nullable=True)
    partida_id = Column(Integer, ForeignKey('partidas.id'))
    multiplicador = Column(Integer, nullable=False, default=1)
    
    def __init__(self,tipo,probabilidad,duracion,enfriamiento):
        #arreglar tipo
        self.tipo = tipo
        self.probabilidad = probabilidad
        self.duracion = duracion
        self.enfriamiento = enfriamiento
        self.tiempo_activacion = None
        self.activo = False
        self.multiplicador = 1


    def efectoEvento(self,partida,resultado):
        if resultado == True:
            if self.tipo == 1:
                self.multiplicador += 0.3
                aldeanos = [mejora for mejora in partida.mejoras if isinstance(mejora, Aldeano)]
                lenyadores = [mejora for mejora in partida.mejoras if isinstance(mejora, Lenyador)]
                arqueros = [mejora for mejora in partida.mejoras if isinstance(mejora, Arquero)]
                picaros = [mejora for mejora in partida.mejoras if isinstance(mejora, Picaro)]
                magos = [mejora for mejora in partida.mejoras if isinstance(mejora, Mago)] 
                bardos = [mejora for mejora in partida.mejoras if isinstance(mejora, Bardo)]
                soldados = [mejora for mejora in partida.mejoras if isinstance(mejora, Soldado)]
                druidas = [mejora for mejora in partida.mejoras if isinstance(mejora, Druida)]
                brujas = [mejora for mejora in partida.mejoras if isinstance(mejora, Bruja)]
                nobles = [mejora for mejora in partida.mejoras if isinstance(mejora, Noble)]
                # Obtener los últimos 5
                aldeanos_a_borrar = aldeanos[round(-5*self.multiplicador):]
                lenyadores_a_borrar = lenyadores[round(-3*self.multiplicador):]
                arqueros_a_borrar = arqueros[round(-5*self.multiplicador):]
                picaros_a_borrar = picaros[round(-5*self.multiplicador):]
                magos_a_borrar = magos[round(-6*self.multiplicador):]
                bardos_a_borrar = bardos[round(-4*self.multiplicador):]
                soldados_a_borrar = soldados[round(-6*self.multiplicador):]
                druidas_a_borrar = druidas[round(-3*self.multiplicador):]
                brujas_a_borrar = brujas[round(-4*self.multiplicador):]
                nobles_a_borrar = nobles[round(-5*self.multiplicador):]
                # Eliminar esos objetos de la lista completa
                for aldeano in aldeanos_a_borrar:
                    partida.mejoras.remove(aldeano)

                for lenyador in lenyadores_a_borrar:
                    partida.mejoras.remove(lenyador)

                for arquero in arqueros_a_borrar:
                    partida.mejoras.remove(arquero)

                for picaro in picaros_a_borrar:
                    partida.mejoras.remove(picaro)

                for mago in magos_a_borrar:
                    partida.mejoras.remove(mago)

                for bardo in bardos_a_borrar:
                    partida.mejoras.remove(bardo)
                
                for soldado in soldados_a_borrar:
                    partida.mejoras.remove(soldado)

                for druida in druidas_a_borrar:
                    partida.mejoras.remove(druida)

                for bruja in brujas_a_borrar:
                    partida.mejoras.remove(bruja)

                for noble in nobles_a_borrar:
                    partida.mejoras.remove(noble)
                    
                partida.oro = partida.oro - (partida.oro * 0.6) 
                self.tiempo_activacion = time.get_ticks()
                self.activo = True

            elif self.tipo == 2 and not self.activo:
                self.multiplicador += 0.1
                partida.oro_por_click *= round(10*self.multiplicador)
                self.tiempo_activacion = time.get_ticks()
                self.activo = True  # <--- MARCAR COMO ACTIVO

    def sucedeEvento(self):
        num = random.random()
        if not num > self.probabilidad and not num < 0:
            return True
        
        return False
    
    def desactivarEvento(self, partida):
        if self.tipo == 1:
            self.activo = False

        if self.tipo == 2:
            partida.oro_por_click = int(partida.oro_por_click / (10*self.multiplicador))
            self.activo = False

    def verificarDuracion(self, partida, tiempo_actual):
        if self.duracion is not None and self.activo:
            tiempo_transcurrido = (tiempo_actual - self.tiempo_activacion) / 1000
            if tiempo_transcurrido >= self.duracion:
                self.desactivarEvento(partida)
                self.activo = False  # <--- IMPORTANTE
                return True
            
        return False
    
    def nuevaInstancia(self):
        new_tipo = self.tipo 
        new_probabilidad = self.probabilidad 
        new_duracion = self.duracion 
        new_enfriamiento = self.enfriamiento
        new_tiempo_activacion = self.tiempo_activacion
        new_activo = self.activo 

        new_evento = Evento(new_tipo,new_probabilidad,new_duracion,new_enfriamiento)
        return new_evento
