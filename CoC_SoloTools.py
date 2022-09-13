import Dice
import random
import enum

class DegreeOfSuccess(enum.IntEnum):
    ExtremeFailure = 0,
    Failure = 1,
    RegularSuccess = 2,
    HardSuccess = 3,
    ExtremeSuccess = 4

class DifficultyModifier(enum.IntEnum):
    Impossible = -60,
    HighlyUnlikely = -40,
    Unlikely = -20,
    Possible = 0,
    Likely = 20,
    HighlyLikely = 40,
    Certainty = 60


class SoloPlayerJournal:
    title = ''
    events = []
    
    def __init__(self, Title):
        self.events = []
        self.title = Title
        
    def add_entry(self, DateTime, Entry):
        self.events.append([DateTime, Entry])

class Contestant:
    name = ''
    player_stat = 0
    result = ''
    modifier = ''

    def __init__(self, Name, PlayerStat, Modifier=''):        
        self.name = Name
        self.player_stat = PlayerStat
        self.modifier = Modifier.lower()
    
        
class SoloGameTools:
#    DieBag = {
#    'D4' : Dice.Dice(4),
#    'D6' : Dice.Dice(6),
#    'D8' : Dice.Dice(8),
#    'D10' : Dice.Dice(10),
#    'D12' : Dice.Dice(12),
#    'D20' : Dice.Dice(20),
#    'D100' : Dice.Dice(100)}    

    @staticmethod
    def get_table_pages():
        pages = {'Clues' : 45, 'Verbs': 40, 'Random Creature' : 36,
                 'Random NPC' : 29, 'Mythos Points' : 26, 'Dice Roll' : 26,
                 'Danger' : 25, 'Discovery' : 23, 'Development' : 22,
                 'Direction' : 21, 'Downtime Disturbance' : 21, 'Interacting with NPCs' : 31,
                 'Basic NPC Stats': 31, 'Monster Characteristics' : 37,
                 'Auditory Effect' : 48, 'Visual Effect' : 49,
                 'Rumors' : 51, 'Random Event' : 55, 'Location Tables' : 60,
                 'Likelihood' : 5, 'Quick Reference' : 9, 'Generating a Scenario' : 10,
                 'Quest Source' : 14, 'Mythos Creatures Tables' : 36, 'Tone of Exchange': 31,
                 'Outcome' : 31, 'Gender' : 30, 'NPC Keyword Modifier' : 30,
                 'NPC Occupation Table': 29}
        for key, val in sorted(pages.items()):
            print('{0}: {1}'.format(key, val))


    @staticmethod
    def get_downtime_disturbance(modifier = 0):
        die = Dice.Dice(100)
        roll = die.Roll() + modifier
        if roll <= 80:
            return 'You are left undisturbed.'
        elif roll > 8 and roll <= 90:
            return 'Mild disturbance - a vision, a dream, hearing something. Roll on Verbs table for details.'
        else:
            return 'A potentially shocking disturbance. Go to Dice Roll table.'        


    @staticmethod
    def get_next_story_direction(MythosPoints = 0):
        die = Dice.Dice(100)
        roll = die.Roll() + MythosPoints
        if roll >= 0 and roll < 20:
            return 'Downtime - Roll to see if you are disturbed p21.'
        elif roll >= 20 and roll < 40:
            return 'Discovery - Roll against Discovery Table p 23'
        elif roll >= 40 and roll < 60:
            return 'Development - Roll against Development Table p22.'
        elif roll >= 60 and roll < 80:
            return 'Dice Roll - Roll Against Dice Roll Table p26'
        elif roll >= 80:
            return 'Danger - Roll against Danger Table p25, then the Verbs Table p40.'
        

    @staticmethod
    def get_half_and_fifth(stat):
        return (int(stat/2), int(stat/5))
    
    @staticmethod
    def yes_no_maybe():
        die = Dice.Dice(100)
        roll = die.Roll()
        if roll >= 0 and roll < 35:
            return 'Yes'
        elif roll >= 35 and roll < 60:
            return 'Maybe'
        elif roll >= 60:
            return 'No'
    
    @staticmethod
    def get_DegreeOfSuccess(stat, roll, modifier=0, allowCriticalFail = False):
        if roll > (stat + modifier):
            if allowCriticalFail and roll >= 95:
                return DegreeOfSuccess.ExtremeFailure
            else:                            
                return DegreeOfSuccess.Failure

        half_and_fifth = SoloGameTools.get_half_and_fifth((stat + modifier))
        if roll <= half_and_fifth[1]:
            return DegreeOfSuccess.ExtremeSuccess
        if roll <= half_and_fifth[0]:
            return DegreeOfSuccess.HardSuccess
        return DegreeOfSuccess.RegularSuccess
    
#    @staticmethod
#    def sanity_roll(SAN, INT, modifier = 0, causedByMythos = False):
#        die = Dice.Dice(100)
#        san_roll = die.Roll()
#        san_dos = SoloGameTools.get_DegreeOfSuccess(SAN, san_roll, modifier)
#
#        return ''

    @staticmethod
    def opposed_skill_roll(Contestant1, Contestant2):
        victor = Contestant1        
        die = Dice.Dice(100)
        c1_roll = die.Roll()
        c2_roll = die.Roll()
        if Contestant1.modifier != '' or Contestant2.modifier != '':
            d10 = Dice.Dice(10)            
            if Contestant1.modifier != '':
                print('Performing {0} modifier roll for {1}'.format(Contestant1.modifier, Contestant1.name))
                ones = d10.Roll()
                possible1 = d10.Roll() * 10
                possible2 = d10.Roll() * 10
                print('Modify rolls: {} {}'.format(ones + possible1, ones + possible2))
                if Contestant1.modifier == 'bonus':
                    c1_roll = ones
                    if possible1 < possible2:
                        c1_roll += possible1
                    else:
                        c1_roll += possible2
                elif Contestant1.modifier == 'penalty':
                    c1_roll = ones
                    if possible1 > possible2:
                        c1_roll += possible1
                    else:
                        c1_roll += possible2

            if Contestant2.modifier != '':
                print('Performing {0} modifier roll for {1}'.format(Contestant2.modifier, Contestant2.name))
                ones = d10.Roll()
                possible1 = d10.Roll() * 10
                possible2 = d10.Roll() * 10
                print('Modify rolls: {} {}'.format(ones + possible1, ones + possible2))
                if Contestant2.modifier == 'bonus':
                    c2_roll = ones
                    if possible1 < possible2:
                        c2_roll += possible1
                    else:
                        c2_roll += possible2
                elif Contestant2.modifier == 'penalty':
                    c2_roll = ones
                    if possible1 > possible2:
                        c2_roll += possible1
                    else:
                        c2_roll += possible2
                
        
        c1_dos = SoloGameTools.get_DegreeOfSuccess(Contestant1.player_stat, c1_roll)
        c2_dos = SoloGameTools.get_DegreeOfSuccess(Contestant2.player_stat, c2_roll)
        print('{0} rolled {1}. {2}.'.format(Contestant1.name, c1_roll, DegreeOfSuccess._member_names_[c1_dos-1]))
        print('{0} rolled {1}. {2}.'.format(Contestant2.name, c2_roll, DegreeOfSuccess._member_names_[c2_dos-1]))
        if c1_dos == DegreeOfSuccess.Failure and c2_dos == DegreeOfSuccess.Failure:
            print('No victor.')
            return None
        
        if(c1_dos != c2_dos):
            if c2_dos > c1_dos:
                victor = Contestant2
        else: #both rolled the same success
            if Contestant1.player_stat != Contestant2.player_stat:
                if Contestant1.player_stat > Contestant2.player_stat:
                    victor = Contestant1
                else:
                    victor = Contestant2
            else: #roll off
                print('Both rolled the same degree of success, Both have the same stat points. ROLL OFF!')
                a = 0
                b = 0
                while a==b:
                    a = die.Roll()
                    b = die.Roll()
                    print('{0} rolled {1}'.format(Contestant1.name, a))
                    print('{0} rolled {1}'.format(Contestant2.name, b))
                if a < b:
                    victor = Contestant1
                else:
                    victor = Contestant2
        
        print('Victor: {0}'.format(victor.name))
        return victor
    
    

#start_stats = [40, 50, 50, 50, 60, 60, 70, 80]        
#random.shuffle(start_stats)   

#custom_stats = [40, 50, 50, 50, 60, 60, 70, 80]        
#cs = {'STR':40,
#      'CON':50,
#      'POW':50,
#      'DEX':50,
#      'APP':60,
#      'SIZ':60,
#      'INT':70,
#      'EDU':80}
#print(start_stats[0]) 
#investgator = Investigator_7_Fast(start_stats)
#investgator.print_character()

#ben = Contestant('Ben', 50, 'bonus')
#dave = Contestant('Dave', 50, 'penalty')
#winner = SoloGameTools.opposed_skill_roll(ben, dave)

#print(DegreeOfSuccess._member_names_)