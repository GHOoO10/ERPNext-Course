''' 
"lambda" is a keyword used to define anonymous functions, also known as lambda functions or lambda expressions.
 Lambda functions are small, one-line functions that don't require a formal definition using the "def" keyword.
  Instead, they can be created quickly using the lambda syntax.

The general syntax of a lambda function is as follows: lambda arguments: expression
'''
# They are often used in conjunction with built-in functions like map(), filter(), and reduce().

#Example 1: Lambda function to filter even numbers from a list
print("Example 1: Lambda function to filter even numbers from a list")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"The even numbers are:  {even_numbers}")  # Output: [2, 4, 6, 8, 10]
print("Example 1 End.")
print("-" * 30)

# Example 2: Lambda function to perform arithmetic operations
print("Example 2: Lambda function to perform arithmetic operations")
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y
}
print("The Two Numbers We Have Tested : 3 , 5")  
print(f"Result for addition is = {operations['add'](5, 3)}")  # Output: 8
print(f"Result for subtract is = {operations['subtract'](5, 3)}")  # Output: 2
print(f"Result for multiply is = {operations['multiply'](5, 3)}")  # Output: 15
print("Example 2 End.")
print("-" * 30)

print("The End...Thanks.")