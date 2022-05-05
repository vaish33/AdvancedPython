# Decorators are a very powerful and useful tool in Python since it allows programmers to 
# modify the behaviour of function or class. Decorators allow us to wrap another function 
# in order to extend the behaviour of the wrapped function, without permanently modifying it.
#  In Decorators, 
# functions are taken as the argument into another function and then called inside the wrapper function.

# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()


#Output: 

Hello, this is before function execution
This is inside the function !!
This is after function execution
