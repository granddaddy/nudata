import unittest
from NuData_Two import Two

class Test_NuData_Two(unittest.TestCase):

	def test_fileLenSmall(self):
		t = Two('sample_small.txt')

		self.assertEqual(
			100, 
			t.fileLength
			)


	# file larger than memory (12GB)
	# thus testing to see whether file is loaded into
	# memory all at once
	# or lazily loaded as per Python specs
	# def test_fileLenSmall(self):
	# 	t = Two('sample_large.txt')

	# 	self.assertEqual(
	# 		1000000000, 
	# 		t.fileLength
	# 		)

	def test_filePartitionFile(self):

		# file of 11 lines should create 2 partitions
		# when partitionLines is 10
		t1 = Two('sample_eleven.txt', 10)


		self.assertEqual(
			11, 
			t1.fileLength
			)

		files = t1.partitionFile()

		self.assertEqual(
			2, 
			len(files)
			)

		self.assertEqual(
			10, 
			Two.fileLineCount(files[0])
			)

		self.assertEqual(
			1, 
			Two.fileLineCount(files[1])
			)
		

		# file of 100 lines should create 10 partitions
		# when partitionLines is 10
		t2 = Two('sample_small.txt', 10)

		files = t2.partitionFile()

		self.assertEqual(
			10, 
			len(files)
			)

		for i in xrange(10):
			self.assertEqual(
				10, 
				Two.fileLineCount(files[i])
				)

if __name__ == '__main__':
	unittest.main()