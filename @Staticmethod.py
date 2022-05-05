#The staticmethod() built-in function returns a static method for a given function.

class Calculator:

  def add_numbers(num1, num2):
    return num1 + num2

# convert add_numbers() to static method
Calculator.add_numbers = staticmethod(Calculator.add_numbers)

sum = Calculator.add_numbers(5, 7)
print('Sum:', sum)

# Output: Sum: 12


#Create a static method using staticmethod()

class Mathematics:

    def addNumbers(x, y):
        return x + y

# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))

#Output:
The sum is: 15