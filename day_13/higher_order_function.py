from collections.abc import Callable

def sum(a: float, b: float) -> float:
    return a + b

def divide(a: float, b: float) -> float:
    return a / b

def multiple(a: float, b: float) -> float:
    return a * b

def subtract(a: float, b: float) -> float:
    return a - b

# Higher Order Function: very useful when listening for events and trigger a particular function
def calculator(a: float, b: float, func: Callable[[float, float], float]) -> float:
    return func(a, b)

operation_result = calculator(a=5.4, b=3.3, func=multiple)
print(operation_result)

