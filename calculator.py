def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

# Main program
while True:
    try:
        # Get input from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Display operation choices
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice = int(input("Enter your choice (1-4): "))
        
        # Perform calculation based on choice
        if choice == 1:
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select between 1 and 4.")
        
        # Ask if user wants to continue
        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != 'yes':
            break
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Thank you for using the calculator!")