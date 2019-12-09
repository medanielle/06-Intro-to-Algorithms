# must be named test_ (in the start of the file name)
import unittest
import tcalc

# inherit from the unittest.TestCase() class
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(tcalc.add(8, 9), 17)
        self.assertEqual(tcalc.add(-1, 1), 0)
        self.assertEqual(tcalc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(tcalc.subtract(10, 5), 5)
        self.assertEqual(tcalc.subtract(-1, 1), -2)
        self.assertEqual(tcalc.subtract(-1, -1), 0)

    def test_multiple(self):
        self.assertEqual(tcalc.multiply(10, 5), 50)
        self.assertEqual(tcalc.multiply(-1, 1), -1)
        self.assertEqual(tcalc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(tcalc.divide(10, 5), 2)
        self.assertEqual(tcalc.divide(-1, 1), -1)
        self.assertEqual(tcalc.divide(-1, -1), 1)

if __name__ == "__main__":
    unittest.main()


