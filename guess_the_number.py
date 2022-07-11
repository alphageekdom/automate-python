from random import randint

secret_number = randint(1, 20)
print('I am thinking of a number between 1 and 20.')


for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break


if guess == secret_number:
    print('Good job! You guessed my number in ' \
        + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was', secret_number)
