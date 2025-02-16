def print_factors(number):
    for i in range(1, number + 1):
        if number % i == 0:
            print(f"{i} is a factor of {number}")


def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a positive integer.")
            return
        print_factors(num)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")


if __name__ == "__main__":
    main()
