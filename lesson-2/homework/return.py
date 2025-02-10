def get_last_digit():
    number = int(input("Enter a number: "))


    last_digit = abs(number) % 10 

    print("The last digit of the number is:", last_digit)
get_last_digit()
