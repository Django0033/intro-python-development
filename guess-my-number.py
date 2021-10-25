import random

magic_number = random.randint(1, 100)
guess = int(input('What is your guess? '))
guess_count = 1

while magic_number != guess:
    if guess < magic_number:
        print('Higher')
        guess = int(input('What is your guess? '))
        guess_count = guess_count + 1
    elif guess > magic_number:
        print('Lower')
        guess = int(input('What is your guess? '))
        guess_count = guess_count + 1

print(f'You guessed it after {guess_count} tries!')
