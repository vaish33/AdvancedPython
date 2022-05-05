### MetaProgramming is the potential for a program to have knowledge of or manipulate itself.
### In a nutshell, we can say metaprogramming is the code that manipulates code.

# A Class is also an object, and just like any other object, it’s an instance of 
# something called Metaclass. A special class type creates these Class objects. 
# The type class is default metaclass which is responsible for making classes. In the above example, 
# if we try to find out the type of Student class, 
# it comes out to be a type. 

class Student:
    pass
 
# Print type of Student class
print("Type of Student class is:", type(Student))

# Output :

Type of Student class is: <class 'type'>

#Metaclass create Classes and Classes creates objects 

def test_method(self):
    print("This is Test class method!")
 
# creating a base class
class Base:
    def myfun(self):
        print("This is inherited method!")
 
# Creating Test class dynamically using
# type() method directly
Test = type('Test', (Base, ), dict(x="atul", my_method=test_method))
 
# Print type of Test
print("Type of Test class: ", type(Test))
 
# Creating instance of Test class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))
 
# calling inherited method
test_obj.myfun()
 
# calling Test class method
test_obj.my_method()
 
# printing variable
print(test_obj.x)

# Output: 

Type of Test class:  <class 'type'>
Type of test_obj:  <class '__main__.Test'>
This is inherited method!
This is Test class method!
atul

