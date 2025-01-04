import unittest
from main import zeta

class TestZetaFunction(unittest.TestCase):
    def test_zeta_function(self):
        # Test known values of the zeta function
        self.assertAlmostEqual(zeta(2), 1.64493, places=5)
        self.assertAlmostEqual(zeta(3), 1.20206, places=5)
        self.assertAlmostEqual(zeta(4), 1.08232, places=5)

    def test_zeta_function_large_s(self):
        # Test with larger values of s
        self.assertAlmostEqual(zeta(10), 1.000994, places=6)

    def test_zeta_function_small_s(self):
        # Test with values of s close to 1
        self.assertAlmostEqual(zeta(1.1), 10.5844, places=4)

if __name__ == '__main__':
    unittest.main()
