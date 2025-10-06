def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if _name_ == "_main_":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
