import unittest
from add import Add


class TestAdd(unittest.TestCase):
	def test_adds_single_number(self):
		self.assertEqual(Add('1'), 1)