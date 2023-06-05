from random import randint

number = randint(1, 10)

number_of_guesses = 0

print('Hello there! '+ ' I am Guessing a number between 1 and 10.. Type your Guessing:')

while number_of_guesses < 3:
    guessed_number = int(input())
    number_of_guesses += 1
    if guessed_number < number:
        print('Your guess is too low.. Try Again:')
    if guessed_number > number:
        print('Your guess is too high.. Try Again:')
    if guessed_number == number:
        break
if guessed_number == number:
    print('Chears! You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('Game Over! You did not guess the number, The number was ' + str(number) 
          + ' .See You In Another Game :)')