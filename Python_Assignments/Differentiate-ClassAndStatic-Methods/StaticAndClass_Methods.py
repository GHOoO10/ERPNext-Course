<<<<<<< HEAD
'''
- Some Important Differences ?        
   { Static methods } :- 
1- Static methods are denoted by the @staticmethod decorator.
2- They do not have access to the class or instance state and behave like regular functions.
3- They are defined within the class for convenience and logical grouping.
4- In the example, add(), subtract(), power() are static methods since they don't rely on any instance or class state.

   { Class methods } :- 
1- Class methods are denoted by the @classmethod decorator.
2- They have access to the class itself via the cls parameter, allowing them to access class-level data and other class methods.
3- In the example, multiply(), circle_area(), and divide() are class methods as they need access to the class-level
attribute pi to perform the calculations.

- When Used or Useful ?
    " Static methods " = are useful when the operation is independent of any instance or class state and 
        doesn't require accessing class-level data. They provide utility functions within the class namespace.

    " Class methods " = are useful when the operation needs access to the class itself, class-level data,
        or other class methods. They allow manipulation of class-level data and provide a way to 
        define alternative constructors or perform class-specific operations.
'''
#Done By : Ghamdan Mohammed Al-Yamani
class GHOoOMath:
    pi = 3.14159

    #Function to perform addition between two numbers.
    @staticmethod
    def add(a, b):
        return a + b

    #Function to perform subtraction between two numbers.
    @staticmethod
    def subtract(a, b):
        return a - b

    #Function to perform multiplication between two numbers.
    @classmethod
    def multiply(cls, a, b):
        return a * b

    #Function to perform division between two numbers.Raises an exception if the divisor is zero.
    @classmethod
    def divide(cls, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")

    #Function to calculate the power of a number.
    @staticmethod
    def power(base, exponent):
        return base ** exponent

    #Function to calculate the area of a circle based on its radius.
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

    '''
    The static methods : add(), subtract(), and power() , respectively.
     They don't rely on any instance or class-level state.

    The class methods : multiply(), divide(), circle_area(), respectively.
     They have access to the class attribute pi and can manipulate class-level data.
    '''



# Calling the static and class methods
sum_result = GHOoOMath.add(5, 3)
difference_result = GHOoOMath.subtract(10, 4)
product_result = GHOoOMath.multiply(4, 6)
quotient_result = GHOoOMath.divide(10, 2)
power_result = GHOoOMath.power(2, 3)
circle_area_result = GHOoOMath.circle_area(3)

# Printing the results
print("Sum : ", sum_result)
print("Difference : ", difference_result)
print("Product : ", product_result)
print("Quotient : ", quotient_result)
print("Power : ", power_result)
print("Circle Area : ", circle_area_result)
=======
'''
- Some Important Differences ?        
   { Static methods } :- 
1- Static methods are denoted by the @staticmethod decorator.
2- They do not have access to the class or instance state and behave like regular functions.
3- They are defined within the class for convenience and logical grouping.
4- In the example, add(), subtract(), power() are static methods since they don't rely on any instance or class state.

   { Class methods } :- 
1- Class methods are denoted by the @classmethod decorator.
2- They have access to the class itself via the cls parameter, allowing them to access class-level data and other class methods.
3- In the example, multiply(), circle_area(), and divide() are class methods as they need access to the class-level
attribute pi to perform the calculations.

- When Used or Useful ?
    " Static methods " = are useful when the operation is independent of any instance or class state and 
        doesn't require accessing class-level data. They provide utility functions within the class namespace.

    " Class methods " = are useful when the operation needs access to the class itself, class-level data,
        or other class methods. They allow manipulation of class-level data and provide a way to 
        define alternative constructors or perform class-specific operations.
'''
#Done By : Ghamdan Mohammed Al-Yamani
class GHOoOMath:
    pi = 3.14159

    #Function to perform addition between two numbers.
    @staticmethod
    def add(a, b):
        return a + b

    #Function to perform subtraction between two numbers.
    @staticmethod
    def subtract(a, b):
        return a - b

    #Function to perform multiplication between two numbers.
    @classmethod
    def multiply(cls, a, b):
        return a * b

    #Function to perform division between two numbers.Raises an exception if the divisor is zero.
    @classmethod
    def divide(cls, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")

    #Function to calculate the power of a number.
    @staticmethod
    def power(base, exponent):
        return base ** exponent

    #Function to calculate the area of a circle based on its radius.
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

    '''
    The static methods : add(), subtract(), and power() , respectively.
     They don't rely on any instance or class-level state.

    The class methods : multiply(), divide(), circle_area(), respectively.
     They have access to the class attribute pi and can manipulate class-level data.
    '''



# Calling the static and class methods
sum_result = GHOoOMath.add(5, 3)
difference_result = GHOoOMath.subtract(10, 4)
product_result = GHOoOMath.multiply(4, 6)
quotient_result = GHOoOMath.divide(10, 2)
power_result = GHOoOMath.power(2, 3)
circle_area_result = GHOoOMath.circle_area(3)

# Printing the results
print("Sum : ", sum_result)
print("Difference : ", difference_result)
print("Product : ", product_result)
print("Quotient : ", quotient_result)
print("Power : ", power_result)
print("Circle Area : ", circle_area_result)
>>>>>>> 2e5a7af (Uploaded my projects for the second lecture In Python on 8-17-2023 for last Thursday)
