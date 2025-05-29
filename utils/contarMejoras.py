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
from entidades.princesa import Princesa
from entidades.reina import Reina
from entidades.rey import Rey
from entidades.upgrade import Upgrade

class contarMejoras:
    @staticmethod
    def contarAldeanos(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Aldeano))
    @staticmethod
    def contarLenyadores(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Lenyador))
    @staticmethod
    def contarArqueros(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Arquero))
    @staticmethod
    def contarPicaros(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Picaro))
    @staticmethod
    def contarMagos(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Mago))
    @staticmethod
    def contarBardos(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Bardo))
    @staticmethod
    def contarSoldados(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Soldado))
    @staticmethod
    def contarClerigos(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Clerigo))
    @staticmethod
    def contarDruidas(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Druida))
    @staticmethod
    def contarBrujas(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Bruja))
    @staticmethod
    def contarNobles(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Noble))
    @staticmethod
    def contarPrincesas(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Princesa))
    @staticmethod
    def contarReinas(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Reina))
    @staticmethod
    def contarReyes(partida):
         return sum (1 for mejora in partida.mejoras if isinstance(mejora, Rey))
    @staticmethod
    def contarMejoras(partida):
        return sum (1 for mejora in partida.mejoras if isinstance(mejora, Upgrade))