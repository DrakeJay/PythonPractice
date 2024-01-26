import random

def game_mode():

    x = int
    x = 0
    x = int(input("You guess the number PRESS 1: \nPC guess your number PRESS 2: "))
    if x == 1:
        guess(10)
    elif x == 2:
        computer_guess(10)
    else:
        ("Please enter 1 or 2")
    

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Wrong, too low!')
        elif guess > random_number:
            print('Wrong, too high!')
    print(f'Dude! You guessed right! How did you know the number was {random_number}?')

def computer_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c':
        if low!= high:
            guess = random.randint(low, high)
        else:
            guess = low
        guess = random.randint(low, high)
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Dude, The Computer guessed your number, {guess}!')

game_mode()