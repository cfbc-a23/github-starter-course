'''
Example drawn from: 
Sweigart, Al. 2015 *Automate the Boring Stuff with Python*
'''

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
    total = 1
    for i in range(n + 1):
        total *= i
    return total

print(factorial(5))