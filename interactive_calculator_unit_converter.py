# Project 01: Interactive Calculator & Unit Converter
# Beginner-friendly Python CLI project

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculator():
    print("\n--- Basic Calculator ---")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    print("\nChoose operation: +  -  *  /")
    operation = input("Enter operation: ").strip()

    if operation == "+":
        print("Result:", a + b)
    elif operation == "-":
        print("Result:", a - b)
    elif operation == "*":
        print("Result:", a * b)
    elif operation == "/":
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operation!")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometres to Miles")
    print("2. Miles to Kilometres")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

    choice = input("Choose conversion (1-4): ").strip()
    value = get_number("Enter value: ")

    if choice == "1":
        print(f"{value} km = {value * 0.621371:.2f} miles")
    elif choice == "2":
        print(f"{value} miles = {value / 0.621371:.2f} km")
    elif choice == "3":
        print(f"{value}°C = {(value * 9/5) + 32:.2f}°F")
    elif choice == "4":
        print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
    else:
        print("Invalid conversion choice!")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("This converter uses the exchange rate entered by you.")
    amount = get_number("Enter amount: ")
    rate = get_number("Enter exchange rate (target currency per 1 source currency): ")

    if amount < 0 or rate <= 0:
        print("Amount cannot be negative and rate must be greater than zero.")
    else:
        print(f"Converted amount: {amount * rate:.2f}")


def main():
    while True:
        print("\n================================")
        print(" INTERACTIVE CALCULATOR")
        print("       & UNIT CONVERTER")
        print("================================")
        print("1. Basic Arithmetic")
        print("2. Unit Conversion")
        print("3. Currency Conversion")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            currency_converter()
        elif choice == "4":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")


if __name__ == "__main__":
    main()
