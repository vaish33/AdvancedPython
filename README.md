# AdvancedPython

How everything is an object in Python ?

Everything in python is an object, and almost everything has attributes and methods. All functions have a built-in attribute __doc__, which returns the doc string defined in the function's source code. The sys module is an object which has (among other things) an attribute called path. And so forth. 

What’s an object? Different programming languages define “object” in different ways. In some, it means that all objects must have attributes and methods; in others, it means that all objects are subclassable. In python, the definition is looser; some objects have neither attributes nor methods and not all objects are subclassable . But everything is an object in the sense that it can be assigned to a variable or passed as an argument to a function

```
class Product:

    unknown_price = "Ask for details"

    def __init__(self, name, price=None):
        self.name = name
        self.price = price

    def display_price(self):
        if self.price is None:
            return self.unknown_price
        return f"{self.price:.2f}"class Product:

  ```
classes are also objects. So, we can point a variable to a class:

``` 
my_class = Product
We now have a variable my_class pointing to the Product class:

my_class
<class 'product.Product'>
And in fact, Product is also just a variable that points to the Product class:

>>> Product
<class 'product.Product'>
So anything that we could do with Product, we could do with my_class

```
Modules are objects too.

So we can point variables to module objects:
```
>>> import math
>>> silly_math = math
```
We've imported the math module and pointed the silly_math variable to the math module object:

modules are mutable objects, meaning you can add attributes to them and you can update attributes on them.
 
Functions are objects too
```
We have a function called greet :

>>> def greet(name="world"):
...     """Greet a user, or the whole world."""
...     print("Hello", name)
...
The one thing you normally do with a function is call it.

This function greet can be called with one argument or with no arguments:

>>> greet()
Hello world
>>> greet("Trey")
Hello Trey
Because functions are objects, we could point another variable, f, to our function object:

>>> f = greet
The variable f points to the greet function now:

>>> f
<function greet at 0x7fe7cd8619d0>
That means anything we could do with greet, we can do with f:

>>> f()
Hello world
Both of these variables point to the same function object.

Just like modules, classes, and class instances, functions have attributes.

There is a __defaults__ attribute that Python adds to every function. This attribute represents the default values for all arguments that that function might accept:

>>> greet.__defaults__
('world',)

```
 
