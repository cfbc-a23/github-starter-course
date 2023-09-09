'''
Example drawn from: 
Sweigart, Al. 2015 *Automate the Boring Stuff with Python*
'''

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
            
if __name__ == '__main__':
    market_2nd = {'ns': 'green', 'ew': 'red'}
    mission_16th = {'ns': 'red', 'ew': 'green'}
    
    switchLights(market_2nd)