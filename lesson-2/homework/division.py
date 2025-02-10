def integer_division_and_remainder(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    quotient = a // b
    remainder = a % b
    return quotient, remainder

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = integer_division_and_remainder(num1, num2)
if isinstance(result, str):
    print(result)
else:
    quotient, remainder = result
    print(f"The result of integer division is {quotient} and the remainder is {remainder}.")