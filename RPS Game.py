import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("\nPlease choose rock, paper, or scissors (or 'quit' to end): ").lower()
        if user_choice == 'quit':
            break
        if user_choice not in choices:
            print("Invalid choice! Please choose again.")
            continue
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        print(f"\n--- Scores ---")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
    print("\nThanks for playing!")
    print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
play_game()
