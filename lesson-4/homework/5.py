def password_checker():
    password = input("Enter your password: ")
    
    if len(password) < 8:
        print("Password is too short.")
        return
    if not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
        return
    
    print("Password is strong.")

password_checker()
