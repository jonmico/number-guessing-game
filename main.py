from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# temporarily print the answer
random_number = random.randint(1, 100)
print(f"Psst, the correct answer is {random_number}.")

difficulty_setting = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_setting == "easy":
    number_of_tries = 10
elif difficulty_setting == "hard":
    number_of_tries = 5

is_number_guessed = False

while number_of_tries > 0 and not is_number_guessed:
    print(f"You have {number_of_tries} left.")
    guess = int(input("Make a guess: "))
    if guess < random_number:
        print("Too low.")
        print("Guess again.")
        number_of_tries -= 1
    elif guess > random_number:
        print("Too high.")
        print("Guess again.")
        number_of_tries -= 1
    elif guess == random_number:
        print(f"You got it! The answer was {random_number}!")
        is_number_guessed = True
