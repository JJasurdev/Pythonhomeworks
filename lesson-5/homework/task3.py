def print_factors(n: int):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            print_factors(num)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
