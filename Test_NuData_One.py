import unittest
from NuData_One import One

class Test_NuData_One_FindDuplicateInArray(unittest.TestCase):

	def setUp(self):
		self.one = One()

	def test_EmptyArray(self):
		self.assertEqual(
			[], 
			self.one.findDuplicateInArray([])
			)

	def test_InvalidType(self):
		with self.assertRaises(TypeError):
			self.one.findDuplicateInArray('a')

		with self.assertRaises(TypeError):
			self.one.findDuplicateInArray({})

		with self.assertRaises(TypeError):
			self.one.findDuplicateInArray({ 1 : 'a', 2 : 'a' })

	def test_FindDuplicateInArray(self):
		self.assertEqual(
			['a', 'b'], 
			self.one.findDuplicateInArray(['a', 'a', 'b', 'b', 'c'])
			)

		# find two pairs of 'a'
		self.assertEqual(
			['a', 'a', 'b'], 
			self.one.findDuplicateInArray(['a', 'a', 'a', 'a', 'b', 'b', 'c'])
			)

		# finds only self.one pair of 'a', with another 'a' in input that cannot be paired
		self.assertEqual(
			['a', 'b'], 
			self.one.findDuplicateInArray(['a', 'a', 'a', 'b', 'b', 'c'])
			)

		# test with more complex types
		# input = [{1 : 'a'}, {1: 'a'}, {2: 'b'}, {3: 'b'}]
		# self.assertEqual(
		# 	[{1: 'a'}],
		# 	self.one.findDuplicateInArray(input)
		# 	)

		# TODO: implementation for non hashable items


class Test_NuData_One_FindDuplicateInDict(unittest.TestCase):

	def setUp(self):
		self.one = One()

	def test_EmptyDict(self):
		self.assertEqual(
			[], 
			self.one.findDuplicateInDict({})
			)

	def test_InvalidType(self):
		with self.assertRaises(TypeError):
			self.one.findDuplicateInDict('a')

		with self.assertRaises(TypeError):
			self.one.findDuplicateInDict([])

		with self.assertRaises(TypeError):
			self.one.findDuplicateInDict(['a', 'a'])


	def test_FindDuplicateInDict(self):
		self.assertEqual(
			['a', 'b'], 
			self.one.findDuplicateInDict({ 1: 'a', 2: 'a', 3: 'b', 4: 'b' })
			)

		# find two pairs of 'a'
		self.assertEqual(
			['a', 'a', 'b'], 
			self.one.findDuplicateInDict({ 1: 'a', 2: 'a', 3: 'b', 4: 'b', 5: 'a', 6: 'a' })
			)

		# finds only self.one pair of 'a', with another 'a' in input that cannot be paired
		self.assertEqual(
			['a', 'b'], 
			self.one.findDuplicateInDict({ 1: 'a', 2: 'a', 3: 'b', 4: 'b', 5: 'a' })
			)



if __name__ == '__main__':
	unittest.main()