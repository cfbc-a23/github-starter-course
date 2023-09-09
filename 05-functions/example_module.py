def f(x=1, z=1):
    '''
    Solves the equation: x**2 + x + z
    Input: x (float or int), z (float or int)
    Returns: Solution to equation (float or int)
    '''
    rv = x ** 2 + x + z
    return rv

if __name__ == "__main__":
    # executes only if run as a script
    x = float(input("Enter a value for x: "))
    z = float(input("Enter a value for z: "))
    print("Result for input x={}, z={}. Output:".format(x, z))
    print(f(x, z))