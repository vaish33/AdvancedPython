#A Closure is a function object that remembers values in enclosing scopes 
# even if they are not present in memory. 

# Python program to illustrate
# closures
def outerFunction(text):
	text = text

	def innerFunction():
		print(text)

	# Note we are returning function
	# WITHOUT parenthesis
	return innerFunction

if __name__ == '__main__':
	myFunction = outerFunction('Hey!')
	myFunction()

#Output:
omkarpathak@omkarpathak-Inspiron-3542:
~/Documents/Python-Programs/$ python Closures.py 
Hey!

#From the above code, closures help to invoke functions outside their scope.
#The function innerFunction has its scope only inside the outerFunction. 
#But with the use of closures, we can easily extend its scope to invoke a function outside its scope.

