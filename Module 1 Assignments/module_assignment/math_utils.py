def add(a, b):
    if not(isinstance(a, (int, float)) & isinstance(b, (int, float))):
        raise ValueError("Please provide valid input")
    return a + b

def subtract(a, b):
    if not(isinstance(a, (int, float)) & isinstance(b, (int, float))):
        raise ValueError("Please provide valid input")
    return a - b

def square(a):
    if not(isinstance(a, (int, float))):
        raise ValueError("Please provide valid input")
    return a ** 2



