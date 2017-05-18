# Write code that will sort the contents of a file. 
# Assume there is one 32-bit number per line of the file. 
# The file contains 5 billion numbers. 
# The computer that is running this has 8 GB of memory 
# and 256 GB of disk space.

# a line has at most a negative character "-", 10 digits, 
# and a new line character
# a line is therefore at most 12B
# 12B * 5 * 10^9 = 60 * 10^9B = 60GB

# log2(60 * 10^9) = 35
# => non-in-place mergesort => 2100GB of additional files

# instead we will implement heapsort on managable files sizes (4GB)
# then merge the sorted files
# 4GB to be safe on 8GB of memory

# 4GB files => 60GB file creates 15 files

# space complexity is only linear to original file
# this is due to save 15 additional files totalling another 60GB

# time complexity totalss nlogn to heapify the partitions
# of the large file
# then linear to merge the files

import heapq
from itertools import islice

class Two:

	def __init__(self, fileName, partitionLines = int(2**32/12)):
		self.partitionLines = partitionLines

		self.fileName = fileName

		self.fileLength = Two.fileLineCount(self.fileName)

	# most efficient way to read file length in Python
	@staticmethod
	def fileLineCount(fileName):
		f = open(fileName, 'r')
		i = -1
		for i, l in enumerate(f):
			pass
		f.close()
		return i + 1

	def createNewPartition(self, partitionCount, partitionStart, partitionEnd):
		partitionCount = partitionCount + 1

		partitionStart = partitionEnd
		partitionEnd = 	min(partitionStart \
							+ self.partitionLines \
							, self.fileLength)

		partitionFileName = 'partitions/' + '%03d' % partitionCount + '_' + \
							self.fileName

		return partitionCount, partitionStart, partitionEnd, partitionFileName

	def partitionFile(self):
		lineCount = 0

		self.partitionFiles = []

		# to get partitionCount to start at 0, pass it -1 to begin
		partitionCount, partitionStart, partitionEnd, partitionFileName = self.createNewPartition(-1, 0, 0)
		partitionFile = open(partitionFileName, 'w')
		self.partitionFiles.append(partitionFileName)

		f = open(self.fileName, 'r')

		for line in f:
			if lineCount >= partitionEnd:
				partitionFile.close()
				partitionCount, partitionStart, partitionEnd, partitionFileName = \
					self.createNewPartition(partitionCount, partitionStart, partitionEnd)
				partitionFile = open(partitionFileName, 'w')
				self.partitionFiles.append(partitionFileName)

			partitionFile.write(line)
			lineCount = lineCount + 1

		partitionFile.close()
		f.close()
		return self.partitionFiles