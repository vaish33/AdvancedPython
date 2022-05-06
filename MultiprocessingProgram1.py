
# importing the multiprocessing module
import multiprocessing

def print_cube(num):
	"""
	function to print cube of given num
	"""
	print("Cube: {}".format(num * num * num))

def print_square(num):
	"""
	function to print square of given num
	"""
	print("Square: {}".format(num * num))

if __name__ == "__main__":
	# creating processes
	p1 = multiprocessing.Process(target=print_square, args=(10, ))
	p2 = multiprocessing.Process(target=print_cube, args=(10, ))

	# starting process 1
	p1.start()
	# starting process 2
	p2.start()

	# wait until process 1 is finished
	p1.join()
	# wait until process 2 is finished
	p2.join()

	# both processes finished
	print("Done!")


# Output:
Square: 100
Cube: 1000
Done!

# Code Explanation :
# 1. To import the multiprocessing module, we do:
#       import multiprocessing 

# 2. To create a process, we create an object of Process class. It takes following arguments:
#    target: the function to be executed by process
#    args: the arguments to be passed to the target function
#    Note: Process constructor takes many other arguments also which will be discussed later. 
#          In above example, we created 2 processes with different target functions:

#    p1 = multiprocessing.Process(target=print_square, args=(10, ))
#    p2 = multiprocessing.Process(target=print_cube, args=(10, ))

#  3. To start a process, we use start method of Process class.
#     p1.start()
#     p2.start()

#  4. As a result, the current program will first wait for the completion of p1 and then p2. 
#     Once, they are completed, the next statements of current program are executed.

