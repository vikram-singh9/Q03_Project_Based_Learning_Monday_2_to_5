import random

print('Welcome to the number guessing game! \nYou have 5 attempts to win the game between 50 to 100 \nGood luck!')

number_to_guess = random.randrange(50,100)
print(number_to_guess)
chance:int = 5
guess_counter = 0

while guess_counter < chance:
    guess_counter += 1
    user_guess = int(input('Enter your guess number!'))

    if user_guess == number_to_guess:
        print(f"congratulations! You guessed it right {user_guess} and random number was {number_to_guess} in {guess_counter} attempts! you won🎉")
        break
    elif guess_counter >= chance and user_guess != number_to_guess:
        print(f"sorry out of attempts! better luck next time! the number was {number_to_guess}😁")
    elif user_guess > number_to_guess:
        print("You guess is too high! try again")
    elif user_guess < number_to_guess:
        print("You guess to low! try again")
