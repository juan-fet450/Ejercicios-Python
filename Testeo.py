import unittest
from FirstPractice import parOimpar
class MyTestCase(unittest.TestCase):
    def test_ejercicio1(self):
        self.assertEqual("impar", parOimpar(3))


if __name__ == '__main__':
    unittest.main()
