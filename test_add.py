import unittest
from add import Add


class TestAdd(unittest.TestCase):
	def test_adds_single_number(self):
		self.assertEqual(Add('1'), 1)

	def test_adds_two_coma_separated_digits(self):
		self.assertEqual(Add('1,2'), 3)

	def test_adds_three_coma_separated_digits(self):
		self.assertEqual(Add('1,2,3'), 6)

	def test_adds_10_coma_separated_digits(self):
		self.assertEqual(Add('1,2,3,4,5,6,7,8,9,10'), 55)

	def test_adds_tnegative_numbers(self):
		self.assertEqual(Add('1,2,3,-1'), 6)

	def test_empty_before_coma(self):
		self.assertEqual(Add(',2,3'), 5)

	def test_empty_after_coma(self):
		self.assertEqual(Add('1,2,'), 3)
