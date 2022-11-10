import random

print('Guessing game')
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Three Loop Questions:
#1. What do I want to repeat?
#  ->
#2. What do I want to change each time?
#  ->
#3. How long should we repeat?
#  ->

guesses = 3
user_guess = input("Please enter your guess between 1-10: ")
random_number = random.randrange(1, 10)
i = 0

while i < guesses:
    i+=1
    if int(user_guess) == random_number:
        print('You guessed right!')
        break
    else:
        print('You guessed wrong!')
        print(f'You have {guesses-(i)} guesses left!')
        if i != guesses:
            user_guess = input("Try again: ")
        else:
            print(f'The number was {random_number}!!!')

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
print('\nGuessing Game 2 (HARD)')

guesses = 10
user_guess = input("Please enter your guess between 1-100: ")
random_number = random.randrange(1, 100)
i = 0

while i < guesses:
    i+=1
    if int(user_guess) == random_number:
        print('You guessed right!')
        break
    else:
        if int(user_guess) < random_number:
            print('Your guess is too Low!')
        else:
            print('Your guess is too High!')

        print(f'You have {guesses-(i)} guesses left!')
        if i != guesses:
            user_guess = input("Try again: ")
        else:
            print(f'The Correct number was {random_number}!!!')
