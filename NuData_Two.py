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

# time complexity totals nlogn to heapsort the partitions
# of the large file
# then linear to merge the files

import heapq
from itertools import islice
import sys

class Two:

	def __init__(self, fileName, partitionLines = int(2**27/12), n = None):
		self.partitionLines = partitionLines

		self.fileName = fileName

		if n == None:
			self.fileLength = Two.fileLineCount(self.fileName)
		else:
			self.fileLength = int(n)

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

		f = open(self.fileName, 'r')

		self.partitionFiles = []

		# to get partitionCount to start at 0, pass it -1 to begin
		partitionCount, partitionStart, partitionEnd, partitionFileName = self.createNewPartition(-1, 0, 0)
		currArr = []

		for line in f:
			if lineCount >= partitionEnd:
				self.partitionFiles.append(self.sortFile(currArr, partitionFileName))
				currArr = []
				partitionCount, partitionStart, partitionEnd, partitionFileName = \
					self.createNewPartition(partitionCount, partitionStart, partitionEnd)


			currArr.append(int(line))
			lineCount = lineCount + 1

		if len(currArr) > 0:
			self.partitionFiles.append(self.sortFile(currArr, partitionFileName))
			currArr = []

		f.close()
		return self.partitionFiles

	def sortFile(self, arr, fileName):

		heapq.heapify(arr)

		f = open(fileName, 'w')

		for i in xrange(len(arr)):
			f.write(str(heapq.heappop(arr)))
			if i != len(arr):
				f.write('\n')

		f.close()

		return fileName

	def merge(self):

		if not self.sortedFiles:
			raise Exception("Please call sort")

		files = []
		filesPeek = []

		# TODO utilize smarter file structure to add prefix to name
		outName = 'sorted_' + self.fileName
		out = open(outName, 'w')

		for i in xrange(len(self.partitionFiles)):
			f = open(self.partitionFiles[i], 'r')
			val = f.readline()

			# non-empty line
			if len(val) > 0:
				filesPeek.append(int(val))
				files.append(f)

		while len(filesPeek) > 0:

			minIndex = 0
			minVal = filesPeek[0]

			for i in xrange(len(filesPeek)):
				if filesPeek[i] < minVal:
					minVal = filesPeek[i]
					minIndex = i

			out.write(str(minVal) + '\n')
			newVal = files[minIndex].readline()

			if len(newVal) > 0:
				filesPeek[minIndex] = int(newVal)

			else:
				files.pop(minIndex)
				filesPeek.pop(minIndex)


	def sort(self):
		try:
			self.partitionFiles
		except:
			self.partitionFile()

		self.sortedFiles = True

		return self.merge()

if __name__ == '__main__':

	if (len(sys.argv) < 2):
		print 'usage: python NuData_Two filename [n]'

	else:
		if (len(sys.argv) == 2):
			t = Two(sys.argv[1])
			t.sort()

		if (len(sys.argv) == 3):
			t = Two(sys.argv[1], n = sys.argv[2])
			t.sort()

		else:
			print 'usage: python NuData_Two filename [n]'