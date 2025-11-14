import unittest
from is_number_of_petal_even_or_odd import *


class TestIsNumberOfPetalsEvenOrOdd(unittest.TestCase):
	def test_that_number_of_petals_returns_true_or_false(self):
		actual1 = number_of_petal(2,1)
		expected1 = True
		actual2 = number_of_petal(1,3)
		expected2 = False
		actual3 = number_of_petal(1,1)
		expected3 = False
		self.assertEqual(actual1,expected1)
		self.assertEqual(actual2,expected2)
		self.assertEqual(actual3,expected3)

