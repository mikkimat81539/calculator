def addition(n, k):
    return n + k

def subtraction(n, k):
    return n - k

def multiply(n, k):
    return n * k

def division(n, k):
    if k != 0:
        return n / k
    else:
        return "Cannot divide by zero!"

# Get user input
operation = input("Are you adding, subtracting, multiplying, or dividing? ").strip().lower()
n = int(input("Input the first number: "))
k = int(input("Input the second number: "))

# Perform the operation based on user input
if operation == "adding":
    print("Result:", addition(n, k))
elif operation == "subtracting":
    print("Result:", subtraction(n, k))
elif operation == "multiplying":
    print("Result:", multiply(n, k))
elif operation == "dividing":
    print("Result:", division(n, k))
else:
    print("Invalid operation. Please choose from adding, subtracting, multiplying, or dividing.")
