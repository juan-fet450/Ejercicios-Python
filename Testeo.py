import unittest
from FirstPractice import saberEdad
class MyTestCase(unittest.TestCase):
    def test_ejercicio1(self):
        self.assertEqual(72, saberEdad(0,1998))


if __name__ == '__main__':
    unittest.main()
