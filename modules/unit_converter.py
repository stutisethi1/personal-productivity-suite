def length_converter():

    print("\nLength Converter")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")

    choice = input("Enter choice: ")

    value = float(input("Enter value: "))

    if choice == "1":
        print("Result:", value / 1000, "km")

    elif choice == "2":
        print("Result:", value * 1000, "m")

    else:
        print("Invalid choice")


def temperature_converter():

    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter choice: ")

    value = float(input("Enter value: "))

    if choice == "1":
        result = (value * 9/5) + 32
        print("Result:", result, "°F")

    elif choice == "2":
        result = (value - 32) * 5/9
        print("Result:", result, "°C")

    else:
        print("Invalid choice")


def unit_converter_menu():

    while True:

        print("\n------ Unit Converter ------")
        print("1. Length Converter")
        print("2. Temperature Converter")
        print("3. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            length_converter()

        elif choice == "2":
            temperature_converter()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")
