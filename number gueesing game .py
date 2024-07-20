import random

def number_guessing_game(): #function declaration
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed: 
        try:
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please guess a number within the range of 1 to 100.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()  #function call
