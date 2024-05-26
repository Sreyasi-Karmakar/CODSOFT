import random
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (1..rock, 2..paper, or 3..scissor): ").lower()
        if user_choice in ['1', '2', '3']:
            return user_choice
        else:
            print("Invalid choice. Please choose between 1 to 3")
def get_computer_choice():
    return random.choice(['1', '2', '3'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == '1' and computer_choice == '3') or \
         (user_choice == '2' and computer_choice == '1') or \
         (user_choice == '3' and computer_choice == '2'):
        return "You win"
    else:
        return "Computer wins"
def play_game():
    print("Welcome to Rock, Paper, Scissor Game")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (1..yes/2..no): ").lower()
        if play_again != '1':
            print("Thanks for playing!")
            break

play_game()