# In your favourite programming language (PHP or Python preferred):
# Write code that will find a duplicate value in an array.
# Do the same for dictionaries.

class One:
	'Class for question one of NuData Security Engineer Code Test'
	
	# function that works only on valid input types
	@staticmethod
	def findDuplicateHelper(input):

		ret = []

		if len(input) <= 0:
			return ret
			
		instances = {}

		# first iteration through list to check for instances
		for i in input:

			# increment count in instances if already exists in instances
			if i in instances:
				instances[i] = instances[i] + 1

			# else create first instance in instances
			else:
				instances[i] = 1

		for key in instances:
			val = instances[key]

			# append to ret every pair of instances
			while val >= 2:
				ret.append(key)
				val = val - 2

		return ret

	@staticmethod
	def findDuplicateInArray(input):

		# only does type checking and delegates logic to helper function
		if type(input) is not list:
			raise TypeError('Input must be of type list')

		else:
			return One.findDuplicateHelper(input)

	@staticmethod
	def findDuplicateInDict(input):

		# only does type checking and delegates logic to helper function
		if type(input) is not dict:
			raise TypeError('Input must be of type dict')

		else:
			return One.findDuplicateHelper(input.values())