import random

print('Guessing game')
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
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
