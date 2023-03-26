from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# temporarily print the answer
random_number = random.randint(1, 100)
print(f"Psst, the correct answer is {random_number}.")
