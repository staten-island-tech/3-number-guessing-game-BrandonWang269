import random
random_number = random.randint(1, 10)
while True:
    guess_str = input("Guess the secret number (between 1 and 10): ")

    guess = int(guess_str)

    if guess == random_number:
        print("Correct")
    else:
        print("wrong")

        