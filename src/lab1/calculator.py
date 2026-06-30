def calculate(num1: float, num2: float, operation: str) -> float:
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("division by zero")
        return num1 / num2
    if operation == "**":
        return num1 ** num2
    raise ValueError("unknown operation")

def main() -> None:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /, **): ")
    result = calculate(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()