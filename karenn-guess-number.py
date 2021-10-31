import random

number = random.randint(1, 100)
# guess = int(input("What is your guess? "))
# tries = 1
play_again = "yes"

while play_again == "yes":
    guess = int(input("What is your guess? "))
    tries = 1
    while guess != number:
        guess = int(input("What is your guess? "))
        tries = tries + 1

        if guess > number:
            print("Guess lower")
            # guess = int(input("What is your guess? "))
            # tries = tries + 1
        elif guess < number:
            print("Guess higher")
            # guess = int(input("What is your guess? "))
            # tries = tries + 1
    print("You guessed it!")
    print(f"You made {tries} tries")
    play_again = input("Do you want to play again? ")
    number = random.randint(1, 100)
   
