#The classmethod() is an inbuilt function in Python, which returns a class method for a given function.;

#Syntax: classmethod(function)
#Parameter :This function accepts the function name as a parameter.
#Return Type:This function returns the converted class method.

#We can also use @classmethod decorator for classmethod definition.
#Syntax: 
#     @classmethod
#     def fun(cls, arg1, arg2, ...):

#Where, 
#fun: the function that needs to be converted into a class method
#returns: a class method for function.

# Python program to demonstrate
# use of a class method and static method.
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a
	# Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	def display(self):
		print("Name : ", self.name, "Age : ", self.age)

person = Person('Vaish', 21)
person.display()

#Output

Name :  Vaish Age :  21


