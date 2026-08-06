#inbluilt functions: 
import math as m
print(m.sqrt(16))

# # Global Scope

greeting = "Hi"

def say_hello():
    print(greeting + " from inside the function")
    
say_hello()
print(greeting + " from outside the function")



# # Local Scope
def greet():
    message = "Hello World"
    print(message)
    
greet()
#print(message) --error


# Function with parameters and return value
# def add_numbers():
#     c = a + b
#     return c

# result = add_numbers()
# print("Sum: ", c)

# def function_name(parameters):
#     #Code block
#     return result

#Example 1: Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def print_factorial(n):
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
    
print_factorial(2)

# Example 2: Math Operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"
    
while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "5":
        print("Exiting Program.")
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        print("Result: ", add(num1, num2))
    elif choice == "2":
        print("Result: ", subtract(num1, num2))
    elif choice == "3":
        print("Result: ", multiply(num1, num2))
    elif choice == "4":
        print("Result: ", divide(num1, num2))
    else:
        print("Invclid choice. Please try again.")