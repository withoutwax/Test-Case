import ast

class Test:
	def __init__(self, algorithm, test_cases, data_type = None):
		self.algorithm = algorithm
		self.test_cases = test_cases
		self.data_type = data_type.lower()
		
		self.run(self.algorithm, self.test_cases)
		self.readCustomTCDirectory(self.test_cases, self.data_type)
	
	def run(self, algorithm, test_cases):
		test_cases = self.readCustomTCDirectory(test_cases, self.data_type)
		for test_case in test_cases:
			print(algorithm(test_case))
	
	def printInput(self, algorithm, test_cases):
		print(algorithm)
		print(test_cases)
	
	def readCustomTCDirectory(self, directory, data_type):
		input_file = open(directory, 'r')
		input_data = input_file.read().splitlines()
		input_file.close()
		
		result = []
		if data_type == 'array' or data_type == 'arr':
			for data in input_data:
				result.append(ast.literal_eval(data))
		print(result)
		return result
		
		
		
		