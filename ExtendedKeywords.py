#Extended Keywords : In Python, we can pass a variable number of arguments to a function using special symbols. 
# There are two special symbols:
#Special Symbols Used for passing arguments:-
##1.)*args (Non-Keyword Arguments)
##2.)**kwargs (Keyword Arguments)

#1.)*args (Non-Keyword Arguments) - The special syntax *args in function definitions in python is 
# used to pass a variable number of arguments to a function. It is used to pass a non-key worded, 
# variable-length argument list. 

# Python program to illustrate
# *args for variable number of arguments
from socket import VMADDR_CID_HOST


def myFun(*argv):
	for arg in argv:
		print (arg)

myFun('Hello', 'Welcome', 'to', 'India')

# Output: 
Hello
Welcome
to
India

# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *argv):
	print ("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)

myFun('Hello', 'Welcome', 'to', 'Chennai')

#Output: 
First argument : Hello
Next argument through *argv : Welcome
Next argument through *argv : to
Next argument through *argv : Chennai

#2.)**kwargs (Keyword Arguments)
#The special syntax **kwargs in function definitions in python is used to pass a keyworded, 
#variable-length argument list. We use the name kwargs with the double star. 
#The reason is because the double star allows us to pass through keyword arguments (and any number of them).

# Python program to illustrate
# *kwargs for variable number of keyword arguments

def myFun(**kwargs):
	for key, value in kwargs.items():
		print ("%s == %s" %(key, value))

# Driver code
myFun('Hi' first ='this', mid ='is', last='Vaish')

#Output: 
last == this
mid == is
first == Vaish

# Using *args and **kwargs in same line to call a function

def myFun(*args,**kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('I','like','Coffee',first="I",mid="like",last="Coffee")

#Output: 
args: ('I', 'like', 'Coffee')
kwargs {'first': 'I', 'mid': 'like', 'last': 'Coffee'}

