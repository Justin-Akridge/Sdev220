import unittest

from fractions import Fraction
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(1, result)

    # The first unit test should pass since we assert that it equals 6,
    # while the second test should fail since we assert it should equal 1.

if __name__ == '__main__':
    unittest.main()
