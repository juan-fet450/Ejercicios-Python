import unittest
from FirstPractice import parOimpar
from FirstPractice import edad
class MyTestCase(unittest.TestCase):
    def test_ejercicio1(self):
        self.assertEqual(70, edad(20,2020))


class MyTestCase2(unittest.TestCase):
    def test_ejercicio1(self):
        self.assertEqual("impar", parOimpar(3))


if __name__ == '__main__':
    unittest.main()
