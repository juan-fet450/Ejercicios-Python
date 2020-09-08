import unittest
from FirstPractice import indicepalabra
class MyTestCase(unittest.TestCase):
    def test_ejercicio1(self):
        self.assertEqual("cs", indicepalabra("coronavirus"))


if __name__ == '__main__':
    unittest.main()
