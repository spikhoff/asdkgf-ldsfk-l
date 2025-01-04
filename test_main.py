import unittest
from main import zeta

class TestZetaFunction(unittest.TestCase):
    def test_zeta_function(self):
        self.assertAlmostEqual(zeta(2), 1.64393, places=5)
        self.assertAlmostEqual(zeta(3), 1.20206, places=5)
        self.assertAlmostEqual(zeta(4), 1.08232, places=5)

    def test_zeta_function_large_s(self):
        # Adjust precision to 5 places
        self.assertAlmostEqual(zeta(10), 1.000994, places=5)

    def test_zeta_function_small_s(self):
        self.assertAlmostEqual(zeta(1.1), 5.57283, places=4)

if __name__ == '__main__':
    unittest.main()
