import unittest
from Split_a_string_function import *

class TestSplitAStringFunction(unittest.TestCase):
	def test_that_Split_a_string_splits_string(self):
		actual = Split_a_string("I love Jesus")
		expected = ["I","love","Jesus"]
		self.assertEqual(actual,expected)