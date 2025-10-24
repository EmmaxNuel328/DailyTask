import unittest
from love_is_true_or_false import *


class TestLoveIsTrueOrfalse(unittest.TestCase):
	def test_that_is_love_true_or_false_returns_true_or_false(self):
		actual1 = is_love_true_or_false(2,1)
		expected1 = True
		actual2 = is_love_true_or_false(1,3)
		expected2 = False
		actual3 = is_love_true_or_false(1,1)
		expected3 = False
		self.assertEqual(actual1,expected1)
		self.assertEqual(actual2,expected2)
		self.assertEqual(actual3,expected3)
	#def test_that_number_of_petals
