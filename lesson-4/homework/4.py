import random

def play_game():
    number = random.randint(1, 100)
    attempts = 10
    
    print("I'm thinking of a number between 1 and 100.")
    
    for _ in range(attempts):
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You guessed it right!")
            return
    
    print("You lost. Want to play again?")
    again = input().strip().lower()
    if again in ['y', 'yes', 'ok']:
        play_game()

play_game()
