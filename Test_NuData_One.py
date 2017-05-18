import unittest
from NuData_One import One

class Test_NuData_One_FindDuplicateInArray(unittest.TestCase):

	def test_EmptyArray(self):
		self.assertEqual(
			[], 
			One.findDuplicateInArray([])
			)

	def test_InvalidType(self):
		with self.assertRaises(TypeError):
			One.findDuplicateInArray('a')

		with self.assertRaises(TypeError):
			One.findDuplicateInArray({})

		with self.assertRaises(TypeError):
			One.findDuplicateInArray({ 1 : 'a', 2 : 'a' })

	def test_FindDuplicateInArray(self):
		self.assertEqual(
			['a', 'b'], 
			One.findDuplicateInArray(['a', 'a', 'b', 'b', 'c'])
			)

		# find two pairs of 'a'
		self.assertEqual(
			['a', 'a', 'b'], 
			One.findDuplicateInArray(['a', 'a', 'a', 'a', 'b', 'b', 'c'])
			)

		# finds only One.pair of 'a', with another 'a' in input that cannot be paired
		self.assertEqual(
			['a', 'b'], 
			One.findDuplicateInArray(['a', 'a', 'a', 'b', 'b', 'c'])
			)

		# test with more complex types
		# input = [{1 : 'a'}, {1: 'a'}, {2: 'b'}, {3: 'b'}]
		# self.assertEqual(
		# 	[{1: 'a'}],
		# 	One.findDuplicateInArray(input)
		# 	)

		# TODO: implementation for non hashable items


class Test_NuData_One_FindDuplicateInDict(unittest.TestCase):


	def test_EmptyDict(self):
		self.assertEqual(
			[], 
			One.findDuplicateInDict({})
			)

	def test_InvalidType(self):
		with self.assertRaises(TypeError):
			One.findDuplicateInDict('a')

		with self.assertRaises(TypeError):
			One.findDuplicateInDict([])

		with self.assertRaises(TypeError):
			One.findDuplicateInDict(['a', 'a'])


	def test_FindDuplicateInDict(self):
		self.assertEqual(
			['a', 'b'], 
			One.findDuplicateInDict({ 1: 'a', 2: 'a', 3: 'b', 4: 'b' })
			)

		# find two pairs of 'a'
		self.assertEqual(
			['a', 'a', 'b'], 
			One.findDuplicateInDict({ 1: 'a', 2: 'a', 3: 'b', 4: 'b', 5: 'a', 6: 'a' })
			)

		# finds only One.pair of 'a', with another 'a' in input that cannot be paired
		self.assertEqual(
			['a', 'b'], 
			One.findDuplicateInDict({ 1: 'a', 2: 'a', 3: 'b', 4: 'b', 5: 'a' })
			)



if __name__ == '__main__':
	unittest.main()