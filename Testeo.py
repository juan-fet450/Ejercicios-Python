import unittest
from FirstPractice import edad
class MyTestCase(unittest.TestCase):
    def test_ejercicio1(self):
        self.assertEqual(70, edad(20,2020))


if __name__ == '__main__':
    unittest.main()
