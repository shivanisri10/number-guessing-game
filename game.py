import random

print("""Number Guessing Game
--------------------
How to Play:
- I’ll pick a number between 1 and 100.
- You try to guess it.
- After each guess, I’ll tell you if you’re too high or too low.
- Keep going until you get it right. I’ll show how many tries you needed.
- Play as many rounds as you like. The game keeps track of your best score.
""")

def show_menu():
    print("\n--- Number Guessing Game ---")
    print("1. Play")
    print("2. Check High Score")
    print("3. Exit")

def play_round(high_score):
    number = random.randint(1, 100)
    attempts = 0
    print("\nI have picked a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Pick a number between 1 and 100.")
                continue

            if guess < number:
                print("Too low")
            elif guess > number:
                print("Too high")
            else:
                print(f"Correct! The number was {number}")
                print(f"You got it in {attempts} tries")
                if high_score is None or attempts < high_score:
                    high_score = attempts
                    print("New high score!")
                break

        except ValueError:
            print("That’s not a valid number, Try again!")

    return high_score

def main():
    high_score = None
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number (1–3)")
            continue

        if choice == 1:
            high_score = play_round(high_score)
        elif choice == 2:
            if high_score is None:
                print("No high score yet, Play a round first!")
            else:
                print(f"High Score: {high_score} attempts")
        elif choice == 3:
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3")

main()
