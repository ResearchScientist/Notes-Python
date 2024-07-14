import random

randnum = random.randint(1,10)
guesses = 0

while guesses < 3:
    print('guess a number between 1 and 10: ')
    guess = input()
    guess = int(guess)
    guesses += 1

    if guess == randnum:
        break
    elif guesses == 3:
        break
    else:
        print('guess again')

if guess == randnum:
    print('you got it! Took you ' + str(guesses) + ' guesses!')
else:
    print('out of guesses, the number was ' + str(randnum) + '.')
