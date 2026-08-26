import random


def play_game():
    print("=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("=" * 40)

    low, high = 1, 100
    secret_number = random.randint(low, high)
    attempts = 0
    max_attempts = 7

    print(f"I'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        guess_input = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")

        if not guess_input.strip().lstrip("-").isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < low or guess > high:
            print(f"Please guess a number within the range {low}-{high}.\n")
        elif guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"\nCongratulations! You guessed it in {attempts} attempt(s).")
            return True

    print(f"\nGame over! The number was {secret_number}.")
    return False


def main():
    while True:
        play_game()
        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()