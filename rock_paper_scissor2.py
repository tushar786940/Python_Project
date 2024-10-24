import random

# Function to get user's choice
def get_user_choice():
    print("Choose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("Enter the number of your choice: "))
    
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    else:
        print("Invalid choice. Please select a number between 1 and 3.")
        return get_user_choice()  # Recursively call until valid input

# Function to get computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.\n")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

# Start the game
play_game()