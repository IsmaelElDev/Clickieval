from entidades.aldeano import Aldeano
from entidades.leñador import Lenyador
from entidades.arquero import Arquero
from entidades.mago import Mago
from entidades.bardo import Bardo
from entidades.soldado import Soldado
from entidades.clerigo import Clerigo
from entidades.druida import Druida
from entidades.bruja import Bruja
from entidades.noble import Noble
from entidades.princesa import Princesa
from entidades.reina import Reina
from entidades.rey import Rey

def actualizar_producciones(partida):

    # Contadores de multiplicadores
    multiplicador_bardo = 1.0
    multiplicador_druida = 1.0
    multiplicador_rey = 1.0

    partida.oro_por_segundo = 0
    partida.oro_por_click = 100
    partida.madera_por_segundo = 0
    partida.madera_por_click = 100
    partida.magia_por_segundo = 0

    # Primero: contar cuántos multiplicadores hay
    for mejora in partida.mejoras:
        if isinstance(mejora, Bardo):
            multiplicador_bardo *= mejora.produccion  
        elif isinstance(mejora, Druida):
            multiplicador_druida *= mejora.produccion
        elif isinstance(mejora, Rey):
            multiplicador_rey *= mejora.produccion

    # Ahora: aplicar en cada mejora base
    for mejora in partida.mejoras:
        # Resetear a produccion base
        mejora.produccion = mejora.produccion_base

        # Aplica multiplicadores según el tipo
        if isinstance(mejora, Aldeano) or isinstance(mejora, Lenyador):
            mejora.produccion *= multiplicador_bardo

        if isinstance(mejora, Mago) or isinstance(mejora, Clerigo):
            mejora.produccion *= multiplicador_druida

        # Rey aplica a todos (excepto él mismo)
        if not isinstance(mejora, Rey):
            mejora.produccion *= multiplicador_rey

        # Sumar al total global de la partida
        if isinstance(mejora, Aldeano) or isinstance(mejora, Arquero) or isinstance(mejora, Bruja) or isinstance(mejora, Noble) or isinstance(mejora, Reina):
            partida.oro_por_segundo += mejora.produccion

        if isinstance(mejora, Lenyador):
            partida.madera_por_segundo += mejora.produccion

        if isinstance(mejora, Mago) or isinstance(mejora, Clerigo):
            partida.magia_por_segundo += mejora.produccion

        if isinstance(mejora, Arquero) or isinstance(mejora, Soldado) or isinstance(mejora, Princesa):
            partida.oro_por_click += mejora.produccion
