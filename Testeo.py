import unittest
import FirstPractice
class MyTestCase(unittest.TestCase):
    def test_ejercicio1(self):
        self.assertEqual(11, ejercicio1(5,6))


if __name__ == '__main__':
    unittest.main()
