import unittest
import calculadora
class TestCalculadora(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculadora.sumar(5, 3), 8)
    def test2(self):
        self.assertEqual(calculadora.sumar(-3, -2), -5)
    def test3(self):
        self.assertEqual(calculadora.sumar(0, -4), -4)
    def test4(self):
        self.assertIsNot(calculadora.multiplicar_no_cero(3,1),0,"La función no puede retornar cero")

if __name__ == "__main__":
    unittest.main()