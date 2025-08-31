"""
Number Guessing Game
--------------------
How to Play:
- The computer picks a random number between 1 and 100.
- You try to guess the number.
- After each guess, you’ll be told if it’s too high or too low.
- The game ends when you guess correctly, and shows how many tries it took.
- You can play multiple rounds, and the game will remember your best score.
"""

import random

def get_guess():
    """Ask the user to enter a valid number between 1 and 100."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("That’s not a valid number. Try again.")

def play_round():
    """Play one round of the guessing game and return number of attempts."""
    secret = random.randint(1, 100)
    tries = 0
    print("\nI’ve picked a number between 1 and 100. Can you guess it?")

    while True:
        guess = get_guess()
        tries += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! The number was {secret}.")
            print(f"You guessed it in {tries} tries.")
            return tries

def main():
    """Main loop for the game with high score tracking."""
    best_score = None
    print("Welcome to the Number Guessing Game!")

    while True:
        print("\nMenu:")
        print("1. Play")
        print("2. View Best Score")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            attempts = play_round()
            if best_score is None or attempts < best_score:
                best_score = attempts
                print("New best score!")
        elif choice == "2":
            if best_score is None:
                print("No best score yet. Play a game first.")
            else:
                print(f"Best score so far: {best_score} attempts")
        elif choice == "3":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1, 2, or 3.")

if __name__ == "__main__":
    main()
