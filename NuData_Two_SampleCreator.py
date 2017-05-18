# Write code that will sort the contents of a file. 
# Assume there is one 32-bit number per line of the file. 
# The file contains 5 billion numbers. 
# The computer that is running this has 8 GB of memory and 256 GB of disk space.

import random
import sys

class SampleCreator:
	'Class for question two of NuData Security Engineer Code Test'

	MAXINT = 2147483647
	MININT = -2147483648

	@staticmethod
	def createFiles(filename, n):
		f = open(filename, 'w')

		for i in xrange(n):
			f.write(str(random.randint(SampleCreator.MININT, SampleCreator.MAXINT)))

			if i != n - 1:
				f.write('\n')

		f.close()

if __name__ == '__main__':

	if (len(sys.argv) != 3):
		print 'usage: python NuData_Two_SampleCreator filename n'

	else:
		SampleCreator.createFiles(sys.argv[1], int(sys.argv[2]))