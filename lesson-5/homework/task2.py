def invest(amount: float, rate: float, years: int):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")
def main():
    try:
        principal = float(input("Enter the principal amount: "))
        annual_rate = float(input("Enter the annual rate of return (as a decimal): "))
        years = int(input("Enter the number of years: "))

        invest(principal, annual_rate, years)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
