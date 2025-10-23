import unittest
from convert_to_uppercase_function import *

class TestConvertToUppercaseFunction(unittest.TestCase):
	def test_that_convert_input_to_uppercase(self):
		actual = convert_to_uppercase("emmax")
		expected = "EMMAX"
		self.assertEqual(actual,expected)
	def test_that_convert_input_to_uppercase_raise_valueError(self):
		actual = "EMMAX"
		self.assertRaises(ValueError,convert_to_uppercase,actual)
