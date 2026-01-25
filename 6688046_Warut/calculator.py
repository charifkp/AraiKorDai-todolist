def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def velocity(distance, time):
    if time <= 0:
        raise ValueError("Time must be positive")
    return distance / time

def main():
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide, velocity")
    
    try:
        op = input("Enter operation (add/subtract/multiply/divide/velocity): ").strip().lower()
        
        if op in ["add", "subtract", "multiply", "divide"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if op == "add":
                result = add(a, b)
            elif op == "subtract":
                result = subtract(a, b)
            elif op == "multiply":
                result = multiply(a, b)
            elif op == "divide":
                result = divide(a, b)
        elif op == "velocity":
            distance = float(input("Enter distance: "))
            time = float(input("Enter time: "))
            result = velocity(distance, time)
        else:
            print("Invalid operation")
            return
        
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()