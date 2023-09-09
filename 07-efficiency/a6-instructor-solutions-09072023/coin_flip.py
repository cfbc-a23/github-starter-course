import random
import logging

#logging.disable(logging.DEBUG) # uncomment to disable logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

# make a guess:
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()
    logging.debug('Guess: {}'.format(guess))

# toss coin:
toss = random.randint(0, 1) # 0 is tails, 1 is heads
int_to_str = {0: 'tails', 1: 'heads'} # add to convert from int -> str
toss = int_to_str[toss]

assert type(toss) == type(guess) # not the same type originally ^fixed above

logging.debug('random toss: {}'.format(toss))

# if toss is as guessed, print this, otherwise, prompt to guess again
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess Again!')
    guess = input() # mis-spelling guesss -> guess

    # log and make an assertion if not heads or tails this time
    logging.debug('Guess: {}'.format(guess))
    assert guess == "heads" or guess == "tails", "Must be heads or tails"

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program')