year = 1990

leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

print(str(year) + " is a leap year (True or False): " + str(leap))