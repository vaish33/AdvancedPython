'''
Builder Method is a Creation Design Pattern which aims to “Separate the construction of a complex object from
its representation so that the same construction process can create different representations.” 
It allows you to construct complex objects step by step. Here using the same construction code, 
we can produce different types and representations of the object easily.
It is basically designed to provide flexibility to the solutions to various object creation problems 
in object-oriented programming.
'''

# Abstract course
class Course:

	def __init__(self):
		self.Fee()
		self.available_batches()

	def Fee(self):
		raise NotImplementedError

	def available_batches(self):
		raise NotImplementedError

	def __repr__(self):
		return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)

# concrete course
class DSA(Course):

	"""Class for Data Structures and Algorithms"""

	def Fee(self):
		self.fee = 8000

	def available_batches(self):
		self.batches = 5

	def __str__(self):
		return "DSA"

# concrete course
class SDE(Course):

	"""Class for Software Development Engineer"""

	def Fee(self):
		self.fee = 10000

	def available_batches(self):
		self.batches = 4

	def __str__(self):
		return "SDE"

# concrete course
class STL(Course):

	"""Class for Standard Template Library"""

	def Fee(self):
		self.fee = 5000

	def available_batches(self):
		self.batches = 7

	def __str__(self):
		return "STL"

# Complex Course
class ComplexCourse:

	def __repr__(self):
		return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)

# Complex course
class Complexcourse(ComplexCourse):

	def Fee(self):
		self.fee = 7000

	def available_batches(self):
		self.batches = 6

# construct course
def construct_course(cls):

	course = cls()
	course.Fee()
	course.available_batches()

	return course # return the course object

# main method
if __name__ == "__main__":

	dsa = DSA() # object for DSA course
	sde = SDE() # object for SDE course
	stl = STL() # object for STL course

	complex_course = construct_course(Complexcourse)
	print(complex_course)
