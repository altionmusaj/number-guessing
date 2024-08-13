from art import logo
import random
lives = 10
numbers = list(range(1, 101))
answer = random.choice(numbers)
END_OF_GAME = False
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
def compare(lives, user_choice, answer):
    global END_OF_GAME
    if user_choice > answer:
        print("The right number is smaller.")
        lives -= 1
        if lives == 0:
            print("You've run out of guesses. Game Over.")
            END_OF_GAME = True
    elif user_choice < answer:
        print("The right number is bigger.")
        lives -= 1
        if lives == 0:
            print("You've run out of guesses. Game Over.")
            END_OF_GAME = True
    else:
        END_OF_GAME = True
        print(f"You guessed correctly!! It was {answer}!")
    return lives

select_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if select_difficulty == 'hard':
    lives = 5

while not END_OF_GAME:

    if select_difficulty == 'easy':
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        if any(char.isalpha() for char in guess):
            print("You entered a letter. Please make sure you only enter a number between 1 and 100.")
        else:
            guess = int(guess)
            if guess not in range(1, 101):
                print("You shouldn't guess a number that is not between 1 and 100.")
            else:
                lives = compare(lives, guess, answer)
    else:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        if any(char.isalpha() for char in guess):
            print("You entered a letter. Please make sure you only enter a number between 1 and 100.")
        else:
            guess = int(guess)
            if guess not in range(1, 101):
                print("You shouldn't guess a number that is not between 1 and 100.")
                lives = compare(lives, guess, answer)
            else:
                lives = compare(lives, guess, answer)