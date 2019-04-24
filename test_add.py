import unittest
from add import Add


class TestAdd(unittest.TestCase):
	def test_adds_single_number(self):
		self.assertEqual(Add('1'), 1)

	def test_adds_two_coma_separated_digits(self):
		self.assertEqual(Add('1,2'), 3)

	def test_adds_three_coma_separated_digits(self):
		self.assertEqual(Add('1,2,3'), 6)
