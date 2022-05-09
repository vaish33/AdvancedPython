'''
Factory Method is a Creational Design Pattern that allows an interface or a class to create an object, 
but lets subclasses decide which class or object to instantiate. 
Using the Factory method, we have the best ways to create an object. 
Here, objects are created without exposing the logic to the client, and for creating the new type of object, 
the client uses the same common interface.

Difference between Factory and Abstract factory Pattern:

With the Factory pattern, you produce instances of implementations (Apple, Banana, Cherry, etc.) 
of a particular interface -- say, IFruit.

With the Abstract Factory pattern, you provide a way for anyone to provide their own factory. 
This allows your warehouse to be either an IFruitFactory or an IJuiceFactory, 
without requiring your warehouse to know anything about fruits or juices.

'''
# Python Code for factory method
# it comes under the creational
# Design Pattern

class FrenchLocalizer:

	""" it simply returns the french version """

	def __init__(self):

		self.translations = {"car": "voiture", "bike": "bicyclette",
							"cycle":"cyclette"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class SpanishLocalizer:
	"""it simply returns the spanish version"""

	def __init__(self):
		self.translations = {"car": "coche", "bike": "bicicleta",
							"cycle":"ciclo"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class EnglishLocalizer:
	"""Simply return the same message"""

	def localize(self, msg):
		return msg

def Factory(language ="English"):

	"""Factory Method"""
	localizers = {
		"French": FrenchLocalizer,
		"English": EnglishLocalizer,
		"Spanish": SpanishLocalizer,
	}

	return localizers[language]()

if __name__ == "__main__":

	f = Factory("French")
	e = Factory("English")
	s = Factory("Spanish")

	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))
