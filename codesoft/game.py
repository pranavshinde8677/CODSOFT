import random

def rock_paper_scissors():
    print("=" * 50)
    print("ROCK-PAPER-SCISSORS GAME")
    print("=" * 50)
    
    choices = ['rock', 'paper', 'scissors']
    win_conditions = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    user_score = 0
    computer_score = 0
    rounds = 0
    
    while True:
        rounds += 1
        print(f"\n{'='*20} ROUND {rounds} {'='*20}")
        print(f"SCORE: You {user_score} - {computer_score} Computer")
        
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit Game")
        
        user_choice = input("\nEnter your choice (1-4): ").strip()
        
        if user_choice == '4':
            print("\n" + "="*40)
            print("FINAL SCORE:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            
            if user_score > computer_score:
                print("RESULT: YOU WIN THE GAME! 🎉")
            elif user_score < computer_score:
                print("RESULT: Computer wins the game!")
            else:
                print("RESULT: It's a tie game!")
            print("Thanks for playing!")
            print("="*40)
            break
        
        if user_choice not in ['1', '2', '3']:
            print("Invalid choice! Please enter 1-4")
            continue
        
        # Convert choice to text
        user_move = choices[int(user_choice) - 1]
        computer_move = random.choice(choices)
        
        print(f"\nYour move: {user_move.upper()}")
        print(f"Computer's move: {computer_move.upper()}")
        
        # Determine winner
        if user_move == computer_move:
            result = "IT'S A TIE! 🤝"
        elif win_conditions[user_move] == computer_move:
            result = "YOU WIN THIS ROUND! 🎯"
            user_score += 1
        else:
            result = "COMPUTER WINS THIS ROUND! 💻"
            computer_score += 1
        
        print("\n" + "-"*40)
        print(result)
        print("-"*40)
        
        # Show game rules reminder
        if rounds == 1:
            print("\nGame Rules:")
            print("• Rock beats Scissors")
            print("• Scissors beats Paper")
            print("• Paper beats Rock")
        
        # Ask to continue
        play_again = input("\nPlay another round? (y/n): ").lower()
        if play_again != 'y':
            print("\n" + "="*40)
            print("FINAL SCORE:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            
            if user_score > computer_score:
                print("RESULT: YOU WIN THE GAME! 🎉")
            elif user_score < computer_score:
                print("RESULT: Computer wins the game!")
            else:
                print("RESULT: It's a tie game!")
            print("Thanks for playing!")
            print("="*40)
            break

# Run the game
rock_paper_scissors()