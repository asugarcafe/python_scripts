import random

class Dice:
    ''' A basic random roll dice object 
    '''
    numer_of_sides = 0
    
    def __init__(self, NumberOfSides):
        self.numer_of_sides = NumberOfSides
        
    def Roll(self):
        ''' A random roll of a die
        '''
        if self.numer_of_sides == 10:
            return random.randint(0, self.numer_of_sides -1)
        else:
            return random.randint(1, self.numer_of_sides)

    def RollMany(self, HowMany):
        result = []
        for x in range(1, HowMany+1):
            result.append(self.Roll())
        return result
    
    def GetBestXOfY(self, amount_of_rolls_to_keep, total_amount_of_rolls):
        rolls = []
        for x in range(0, total_amount_of_rolls):
            rolls.append(self.Roll())
        rolls.sort()
        sorted = rolls[::-1]
        return sorted[0:amount_of_rolls_to_keep]
         

#d1 = Dice(1)
#d6 = Dice(6)
#d1000 = Dice(1000)
#print(d1000.Roll())
#print(d100.RollMany(5))
#for x in range(0,10):
#    print(d6.Roll())
#print(d6.GetBestXOfY(3, 5))