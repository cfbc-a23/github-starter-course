def champions(ledger, threshold, num_champs):
    '''
    Computes the first num_champs houses to reach a score
    of at least threshold.

    Inputs:
        ledger: a list of scoring events, where each scoring
            event is a (string, integer) pair consisting of
            the name of the house and the number of points
            that is added to that house's score (which may
            be negative).
        threshold: (positive integer) a house has completed
            the house cup when they meet or exceed this score.
        num_champs: (positive integer) The maximum number
            of houses to include in the list of champions

    Returns: (list of strings) A list of the first num_champs
        houses to complete the house cup, in order.
    '''
    tally = {}
    finishers = []

    # Loop over ledger, tally points for each house recorded in the ledger
    # add house to finishers list if they surpass the required threshold
    for house, points in ledger:
        # Get the current score for house (0 if no current score)
        current_score = tally.get(house, 0)
        if current_score < threshold:
            # add new points in ledger to existing point tally for house
            tally[house] = current_score + points
            if tally[house] >= threshold:
                # if tally surpasses threshold, add to finishers list and
                # break from loop if have reached limit for num_champs
                finishers.append(house)
                if len(finishers) >= num_champs:
                    break
    
    return finishers
