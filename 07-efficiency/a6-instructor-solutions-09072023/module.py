# Write your functions for A5, Q1-Q3, here

'''
1. Complete the function `compute_matching`, which takes two lists of equal
length and returns a list of the same length where the `i`th element is True if
the `i`th elements of the two lists are equal.
'''

def compute_matching(lst1, lst2):
    '''
    Given two lists of equal length, compute a list
    that where the ith element is True if the lists
    match at index i.

    Input: lst1, lst2 (lists)

    Returns: list of bools
    '''
    rv = []
    for i, val in enumerate(lst1):
        rv.append(val == lst2[i])
    return rv

'''
2. Complete the function `compute_matching_indices`, which takes two lists of
equal length and returns a list of the indices where the elements of the two
lists are equal.
'''

def compute_matching_indices(lst1, lst2):
    '''
    Given two lists of equal length, computed a list of
    the indices where the elements of the two lists
    are equal

    Input: lst1, lst2 (lists)

    Returns: list of ints
    '''
    matches = compute_matching(lst1, lst2)
    return [i for i, match in enumerate(matches) if match]

'''
3. Write a python function `lowest_temperature(data, date)` that takes as an
argument a list of lists (of weather data -- as in the prompt on Canvas) and
returns the name of the city with the lowest temperature for the specified date.
'''

data = [["20081114", "Chicago", "50.1", "30.0", "35.7"],
        ["20081114", "Detroit", "45.2", "30.3", "33.4"]]
DATE = 0
CITY = 1
LOW = 3

def lowest_temperature(data, date):
    '''
    Finds the city with the lowest temperature for a specified
    date.

    Input: data (list of lists of strings), date (string of form "YYYYMMDD")
    Returns: City with lowest temp for specified date (str). If no temperatures
    are recorded for date, returns an empty string.

    '''
    # set implausibly high temp + blank city name to begin:
    minCity, minTemp = "", 9999

    # loop through all lines in data and identify overall min. temp
    # Ties broken arbitrarily by first row encountered in data
    for line in data:
        if line[DATE] == date and float(line[LOW]) < minTemp:
            minCity = line[CITY]
            minTemp = float(line[LOW])

    return minCity

"""
A6, Q5: Generate the code for lowest_temperature function from A5, Q3 using
GitHub Copilot. Students should clearly denote that GitHub Copilot generated
code and add notes on what implementation does differently and how it does on
their tests.

Can use the following docstring to generate the functions below:

def lowest_temperature(data, date):
    '''
    Finds the city with the lowest temperature for a specified
    date.

    Input: data (list of lists of strings), date (string of form "YYYYMMDD")
    Returns: City with lowest temp for specified date (str). If no temperatures
    are recorded for date, returns an empty string.

    '''

"""

def lowest_temperature_alt_1(data, date):
    '''
    [Generated with GitHub Copilot using function signature and docstring; 
    Students should mention what this does differerently than their original
    and how it does on their tests; note that this particular function will
    fail on tests 2 and 3 because it will not adjust "city" if the lowest
    temperature appears first in the data]
    
    Finds the city with the lowest temperature for a specified
    date.

    Input: data (list of lists of strings), date (string of form "YYYYMMDD")
    Returns: City with lowest temp for specified date (str). If no temperatures
    are recorded for date, returns an empty string.
    '''
    lowest_temp = float(data[0][LOW])
    city = ""
    for row in data:
        if row[DATE] == date:
            if float(row[LOW]) < lowest_temp:
                lowest_temp = float(row[LOW])
                city = row[CITY]
    return city


def lowest_temperature_alt_2(data, date):
    '''
    [Generated with GitHub Copilot using function signature and docstring; 
    Students should mention what this does differerently than their original
    and how it does on their tests; this one is pretty inefficient with multiple
    loops through the data, but does pass the tests]

    Finds the city with the lowest temperature for a specified
    date.

    Input: data (list of lists of strings), date (string of form "YYYYMMDD")
    Returns: City with lowest temp for specified date (str). If no temperatures
    are recorded for date, returns an empty string.

    '''
    # Your code here
    date_temps = []
    for row in data:
        if row[DATE] == date:
            date_temps.append(row)
    if len(date_temps) == 0:
        return ""
    lowest = date_temps[0]
    for row in date_temps:
        if float(row[LOW]) < float(lowest[LOW]):
            lowest = row
    return lowest[CITY]


def lowest_temperature_alt_3(data, date):
    '''
    [Generated with GitHub Copilot using function signature and docstring; 
    Students should mention what this does differerently than their original
    and how it does on their tests; passes tests, but indexing and min ops
    can be expensive after already looping through full dataset]

    Finds the city with the lowest temperature for a specified
    date.

    Input: data (list of lists of strings), date (string of form "YYYYMMDD")
    Returns: City with lowest temp for specified date (str). If no temperatures
    are recorded for date, returns an empty string.

    '''
    # Initialize empty list to hold temperatures for specified date
    temperatures = []
    # Iterate through data
    for row in data:
        # Check if date matches specified date
        if row[DATE] == date:
            # If it does, add temperature to list
            temperatures.append(float(row[LOW]))
    # Check if temperatures list is empty
    if temperatures:
        # If it is not, return the city with the lowest temperature
        return data[temperatures.index(min(temperatures))][CITY]
    # If it is, return empty string
    else:
        return ""
