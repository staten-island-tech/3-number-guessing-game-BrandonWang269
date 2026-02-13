import random
random_number = random.randint(1, 10)
guess = None
while guess != random_number:
    try:
        guess_number = input('guess the correct number(type random # 1-10)')
        guess = int(guess_number)
        if guess == random_number:
            print("Correct")
        else:
            print('Wrong. Guess again')