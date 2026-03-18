class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b


def calculator_menu():
    calc = Calculator()

    while True:
        print("\n------ Calculator ------")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Back to Main Menu")

        choice = input("Choose operation (1-5): ")

        if choice == "5":
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", calc.add(num1, num2))
            elif choice == "2":
                print("Result:", calc.subtract(num1, num2))
            elif choice == "3":
                print("Result:", calc.multiply(num1, num2))
            elif choice == "4":
                print("Result:", calc.divide(num1, num2))
            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
