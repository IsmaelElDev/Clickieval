import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entidades.aldeano import Aldeano
from entidades.bardo import Bardo
from entidades.partida import Partida
from utils.actualizarProducciones import actualizar_producciones
from entidades.evento import Evento


class TestProduccion(unittest.TestCase):
    def test_produccion_con_1_aldeano(self):
        partida = Partida()
        aldeano = Aldeano("Aldeano", coste=50, produccion_base=1, produccion=1, incPrecio=1.2)
        partida.mejoras.append(aldeano)
        actualizar_producciones(partida)
        self.assertEqual(partida.oro_por_segundo, 1)

    def test_produccion_con_bardo(self):
        partida = Partida()
        aldeano = Aldeano("Aldeano", 50, 1, 1, 1.2)
        bardo = Bardo("Bardo", 500, 0, 2, 1.1)  # multiplica x2
        partida.mejoras.append(aldeano)
        partida.mejoras.append(bardo)
        actualizar_producciones(partida)
        self.assertEqual(partida.oro_por_segundo, 2)

if __name__ == '__main__':
    unittest.main()
