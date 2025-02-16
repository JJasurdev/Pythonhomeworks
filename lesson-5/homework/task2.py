def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")


def main():
    try:
        principal = float(input("Enter the initial investment amount: "))
        annual_rate = float(input("Enter the annual rate of return (as a decimal): "))
        num_years = int(input("Enter the number of years: "))

        print("\nInvestment growth over time:")
        invest(principal, annual_rate, num_years)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    main()
