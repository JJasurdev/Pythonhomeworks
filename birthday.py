def calculate_age():
    name = input("Enter your name: ")
    year_of_birth = int(input("Enter your year of birth: "))
    current_year = 2023 
    age = current_year - year_of_birth
    print(f"{name}, you are {age} years old.")

calculate_age()