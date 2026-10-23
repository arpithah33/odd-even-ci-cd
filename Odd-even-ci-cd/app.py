import sys


def check_odd_even(number):
    """Return whether an integer is odd or even."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number % 2 == 0:
        return "Even"
    return "Odd"


def main():
    """Read a number from the command line and print its result."""
    if len(sys.argv) != 2:
        print("Usage: python app.py <integer>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        result = check_odd_even(number)
        print(result)
    except ValueError:
        print("Error: Please enter a valid integer")
        sys.exit(1)


if __name__ == "__main__":
    main()