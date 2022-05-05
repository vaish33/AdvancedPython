#Managing Resources : In any programming language, the usage of resources like file operations or 
# database connections is very common. But these resources are limited in supply. 
# Therefore, the main problem lies in making sure to release these resources after usage. 
# If they are not released then it will lead to resource leakage and may cause the system to 
# either slow down or crash. It would be very helpful if user have a mechanism for the 
# automatic setup and teardown of resources.In Python, it can be achieved by the usage of 
# context managers which facilitate the proper handling of resources. 
# The most common way of performing file operations is by using the with keyword as shown below:

# Python program showing
# a use of with keyword

with open("test.txt") as f:
	data = f.read()


# Next example, take file management. 
# When a file is opened, a file descriptor is consumed which is a limited resource. 
# Only a certain number of files can be opened by a process at a time. 
# The following program demonstrates it.

file_descriptors = []
for x in range(100000):
	file_descriptors.append(open('test.txt', 'w'))

#Output:

Traceback (most recent call last):
  File "context.py", line 3, in 
OSError: [Errno 24] Too many open files: 'test.txt'

#Creating a Context Manager :When creating context managers using classes, 
# user need to ensure that the class has the methods: __enter__() and __exit__(). 
# The __enter__() returns the resource that needs to be managed and the __exit__() 
# does not return anything but performs the cleanup operations.
#First, lets create a simple class called ContextManager to understand the basic structure of 
# creating context managers using classes, as shown below:

# Python program creating a
# context manager

class ContextManager():
	def __init__(self):
		print('init method called')
		
	def __enter__(self):
		print('enter method called')
		return self
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		print('exit method called')


with ContextManager() as manager:
	print('with statement block')

#Output
init method called
enter method called
with statement block
exit method called
