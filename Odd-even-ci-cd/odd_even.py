def check_odd_even(number):
    if isinstance(number, bool) or not isinstance(number, int):
        raise ValueError("Please enter an integer")
    return "Even" if number % 2 == 0 else "Odd"


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        print(check_odd_even(number))
    except ValueError:
        print("Invalid input. Please enter an integer.")