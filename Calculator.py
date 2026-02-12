# calculator.py

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


def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero is not allowed"
    return a % b


def square(a):
    return a * a


def show_menu():
    print("\n===== Calculator Menu =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")
    print("6. Square (x²)")
    print("7. Exit")


def main():
    print("Welcome to CLI Calculator")

    while True:
        show_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Exiting Calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please try again.")
            continue

        try:
            # Square needs only one number
            if choice == "6":
                num = float(input("Enter number: "))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)

        elif choice == "4":
            result = divide(num1, num2)

        elif choice == "5":
            result = modulo(num1, num2)

        elif choice == "6":
            result = square(num)

        print("Result:", result)


if __name__ == "__main__":
    main()
