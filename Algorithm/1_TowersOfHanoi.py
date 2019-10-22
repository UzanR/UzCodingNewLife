def TowersOfHanoi(numberOfDisks, startPeg=1, endPeg=3):
    if numberOfDisks:
        TowersOfHanoi(numberOfDisks-1, startPeg, 6-startPeg-endPeg)
        print ('Move disk ' + str(numberOfDisks) + ' from ' + str(startPeg) + ' to peg ' + str(endPeg))
        TowersOfHanoi(numberOfDisks-1, 6-startPeg-endPeg, endPeg)

TowersOfHanoi(4, 1, 3)