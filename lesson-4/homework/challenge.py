import random

def play_rps():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        computer_choice = random.choice(options)
        player_choice = input("Choose rock, paper, or scissors: ").strip().lower()

        if player_choice not in options:
            print("Invalid choice, try again.")
            continue

        print(f"Computer chose {computer_choice}.")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score: Player {player_score} - Computer {computer_score}\n")

    if player_score == 5:
        print("Congratulations! You won the match!")
    else:
        print("Computer won the match. Better luck next time!")

play_rps()
