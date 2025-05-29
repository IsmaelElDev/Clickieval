import unittest
import sys
import os

# Asegurar que se pueda importar el resto del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entidades.partida import Partida
from entidades.aldeano import Aldeano
from entidades.evento import Evento
from servicios.database_operations import guardar_partida, cargar_partida
from servicios.database import create_tables

class TestDatabaseOperations(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Asegurarse de que las tablas existan antes de correr cualquier test
        create_tables()

    def test_guardar_partida(self):
        partida = Partida("Partida Test")
        partida.oro = 1000

        # Guardar la partida
        partida_guardada = guardar_partida(partida)

        # Verificar que tiene ID y se guardó
        self.assertIsNotNone(partida_guardada.id)
        self.assertEqual(partida_guardada.nombre, "Partida Test")
        self.assertEqual(partida_guardada.oro, 1000)

    def test_cargar_partida_con_mejoras(self):
        # Crear y guardar una partida con un aldeano
        partida = Partida("Partida con Aldeano")
        aldeano = Aldeano(nombre="Aldeano", coste=10, produccion_base=1, produccion=1, incPrecio=1.1)
        aldeano.partida = partida
        partida.mejoras.append(aldeano)

        partida_guardada = guardar_partida(partida)
        partida_id = partida_guardada.id

        # Cargar la partida
        partida_cargada = cargar_partida(partida_id)

        self.assertIsNotNone(partida_cargada)
        self.assertEqual(partida_cargada.id, partida_id)
        self.assertEqual(len(partida_cargada.mejoras), 1)
        self.assertEqual(partida_cargada.mejoras[0].nombre, "Aldeano")
        self.assertGreaterEqual(partida_cargada.oro_por_segundo, 1)

if __name__ == '__main__':
    unittest.main()
