from calculator_art import calculator_logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("⚠️  Can't divide by zero!")
        return None
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(calculator_logo)
    n1 = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:
        print(f"\nCurrent number: {n1}")
        for symbol in operations:
            print(symbol)
        op = input("Pick an operation: ")

        if op not in operations:
            print("❌ Invalid operation, try again.")
            continue

        n2 = float(input("What's the next number?: "))
        result = operations[op](n1, n2)

        if result is None:
            continue

        print(f"\n{'='*30}")
        print(f"  {n1} {op} {n2} = {result}")
        print(f"{'='*30}")

        choice = input(f"\nType 'y' to continue calculating with {result}\nType 'n' to start a new calculation\nType 'q' to quit\n> ")

        if choice == 'y':
            n1 = result
        elif choice == 'n':
            calculator()
            return
        else:
            print("\n👋 Thanks for calculating. Bye!")
            should_continue = False

calculator()

