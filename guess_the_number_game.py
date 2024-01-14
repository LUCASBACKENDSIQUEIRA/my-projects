import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Initialize a variable for the user's guess
user_guess = 0 

while user_guess != random_number:
    # Take the user's guess as input
    user_guess = int(input("Guess the number (between 1 and 100): "))

# Compare the user's guess with the random number
    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number:", random_number)



