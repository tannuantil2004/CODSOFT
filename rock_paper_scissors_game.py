import random

def determine_winner(u1_name, u1_choice, computer_choice):
    if u1_choice == computer_choice:
        return "It's a tie!"
    elif (u1_choice == 1 and computer_choice == 3) or \
         (u1_choice == 2 and computer_choice == 1) or \
         (u1_choice == 3 and computer_choice == 2):
        return f"{u1_name} wins!"
    else:
        return "Computer wins!"

def get_choice(user_name):
    while True:
        try:
            choice = int(input(f"{user_name}, enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please choose 1 for Rock, 2 for Paper, or 3 for Scissors.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game(u1_name):
    user_score = 0
    computer_score = 0
    
    while True:
        print(f"\nScore - {u1_name}: {user_score}  Computer: {computer_score}")
        u1_choice = get_choice(u1_name)
        computer_choice = random.randint(1, 3)
        print(f"Computer chooses: {computer_choice}")
        
        result = determine_winner(u1_name, u1_choice, computer_choice)
        print(result)
        
        if result == f"{u1_name} wins!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
            print(f"{u1_name} lost!")
        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Game ended. Final scores:")
            print(f"{u1_name}: {user_score}  Computer: {computer_score}")
            break

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")
    
    u1_name = input("Enter your name: ")
    play_game(u1_name)

if __name__ == "__main__":
    main()
