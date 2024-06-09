def play_game():
    print("Let's play Rock Paper Scissors")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = input("Enter your choice: ")
    print("User choice: ", user_choice)
    # Computer choice
    computer_choice = "Rock"
    print("Computer choice: ", computer_choice)
    # Determine the winner
    if user_choice == "1" and computer_choice == "Scissors":
        print("User wins!")
    elif user_choice == "2" and computer_choice == "Rock":
        print("User wins!")
    elif user_choice == "3" and computer_choice == "Paper":
        print("User wins!")
    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("Computer wins!")

def main():
    while True:
        print("Rock Paper Scissors Game")
        print("1. Play Game")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            play_game()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()