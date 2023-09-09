'''
Example drawn from: 
Sweigart, Al. 2015 *Automate the Boring Stuff with Python*
'''

import logging
#logging.disable(logging.CRITICAL) # uncomment to disable logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    '''
    Calculates the factorial of a number (n). Examples:
    Factorial 3 is 1 * 2 * 3, or 6
    Factorial 4 is 1 * 2 * 3 * 4, or 24
    etc.
    Input: n (integer)
    Output: factorial of input (n)
    
    IMPORTANT NOTE: THIS FUNCTION HAS A BUG
    '''
    logging.debug('Start of factorial({})'.format(n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is {}, total is {}'.format(str(i), str(total)))
    logging.debug('End of factorial({})'.format(n))
    return total

print(factorial(5))
logging.debug('End of program')