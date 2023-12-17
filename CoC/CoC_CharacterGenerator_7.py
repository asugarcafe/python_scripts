import Dice

class SkillList:
    skills = {}
    
    def __init__(self, DEX = 1, EDU = 1):
        self.skills = SkillList.get_base_skill_list(DEX, EDU);   
        
    def get_skill(self, name):
        return self.skills[name]    

    def set_skill(self, name, NewValue):
        del(self.skills[name])
        self.skills[name] = NewValue
        
    @staticmethod
    def get_base_skill_list(DEX = 1, EDU = 1):
        return {'Accounting' : 5,
        'Acting' : 5,
        'Animal Handling' : 5,
        'Anthropology' : 1,
        'Appraise' : 5,
        'Archaeology' : 1,
        'Art and Craft' : 5,
        'Artillery' : 1,
        'Astronomy' : 1,
        'Axe' : 15,
        'Biology' : 1,
        'Botany' : 1,
        'Bow' : 15,
        'Brawl' : 25,
        'Chainsaw' : 10,
        'Charm' : 15 ,
        'Chemistry' : 1,
        'Climb' : 20 ,
        'Computer Use' : 5,
        'Credit Rating' : 0,
        'Cryptography' : 1,
        'Cthulhu Mythos' : 0,
        'Demolitions' : 1,
        'Disguise' : 5,
        'Diving' : 1,
        'Dodge' : int(DEX/2),
        'Drive Auto' : 20,
        'Electrical Repair' : 10,
        'Electronics' : 1,
        'Fast Talk' : 5,
        'Fine Art' : 5,
        'First Aid' : 30,
        'Flail' : 10,
        'Flamethrower' : 10,
        'Forensics' : 5,
        'Forgery' : 1,
        'Garrote' : 15,
        'Geology' : 1,
        'Handgun' : 20,
        'Heavy Weapons' : 10,
        'History' : 5,
        'Hypnosis' : 1,
        'Intimidate' : 15,
        'Jump' : 20,
        'Language Other' : 1,
        'Language Own' : EDU,
        'Law' : 5,
        'Library Use' : 20,
        'Listen' : 20,
        'Locksmith' : 1,
        'Machine Gun' : 10,
        'Mathematics' : 1,
        'Mechanical Repair' : 10,
        'Medicine' : 1 ,
        'Meteorology' : 1,
        'Natural World' : 10,
        'Navigate' : 10,
        'Occult' : 5,
        'Operate Heavy Machinery' : 1,
        'Persuade' : 10,
        'Pharmacy' : 1,
        'Photography' : 5,
        'Physics' : 1,
        'Pilot' : 1,
        'Psychoanalysis' : 1,
        'Psychology' : 10,
        'Read Lips' : 1,
        'Ride' : 5,
        'Rifle' : 25,
        'Science' : 1,
        'Shotgun' : 25,
        'Sleight of Hand' : 10,
        'Spear' : 20,
        'Spot Hidden' : 25,
        'Stealth' : 20 ,
        'Submachine Gun' : 15,
        'Survival' : 10,
        'Sword' : 20,
        'Swim' : 20 ,
        'Throw' : 20,
        'Track' : 10,
        'Whip' : 5,
        'Zoology' : 1}

class InvestigatorItem:
    name = ''
    damage_roll = '1d1' 
    weight = .1 
          
    def __init__(self, Name, DamagaRoll = '1d1', Weight = .1):
        self.name = Name
        self.damage_roll = DamagaRoll
        self.weight = Weight
        
    def print_item(self):
        return '"{0}", {1}, {2} lbs.'.format(self.name, self.damage_roll, self.weight)
        
class InvestigatorWeapon(InvestigatorItem):
    use_range = 'Melee'
    attacks_per_round = 1
    ammo = 1
          
    def __init__(self, Name, DamageRoll = '1d1', UseRange = 'Melee', Weight = .1, AttackPerRound = 1, Ammo = 0):
        self.name = Name
        self.damage_roll = DamageRoll
        self.weight = Weight
        self.attacks_per_round = AttackPerRound
        self.ammo = Ammo
        self.use_range = UseRange

    def print_item(self):
        return '"{0}", {1}, {5} range, {2} lbs., {3} attacks per round, {4} rounds of ammo.'.format(self.name, self.damage_roll, self.weight, self.attacks_per_round, self.ammo, self.use_range)
        
class InvestigatorBackpack:
    items = []
    
    def __init__(self):
        self.items = []
               
    def get_item(self, Name):
        result = []
        for item in self.items:
            if item.name.lower() == Name.lower():
                result.append(item)
        return result

    def drop_item(self, Name):
        result = []
        for item in self.items:
            if item.name.lower() != Name.lower():
                result.append(item)
        self.items = result

    def add_item(self, Item):
        self.items.append(Item)

    def print_backpack(self):
        for val in self.items:
            print('{0}'.format(val.name))

class Investigator_7_Fast:
    NAME = 'Investigator 1'
    STR = 0
    CON = 0
    POW = 0
    DEX = 0
    APP = 0
    SIZ = 0
    INT = 0
    EDU = 0   
    
    SAN = 0
    LUCK = 0
    IDEA = 0
    KNOW = 0
    DamageBonus = '0'
    BUILD = 0
    HIT_POINT = 0
    MAGIC_POINT = 0
#    SANITY_POINT = 0    
    MYTHOS_POINTS = 0    
#    INCOME = 0
    CAREER_SKILL_POINTS = 'one at 70%, two at 60%, three at 50% and three at 40% (set the skills directly to these values and ignore the skill base values written next to each skill on the investigator sheet).'
    PERSONAL_INTEREST_SKILL_POINTS = 'Pick four non-occupation skills and boost them by 20% (adding 20 to the skill base values listed on the investigator sheet).'
#    MIN_AGE = 0 
    CAREER = ''
    SKILL_LIST = {}
    BACKPACK = None   
    INSIGHT_POINT = 0    
    
    def __init__(self, Name, presets, Career = ''):
        self.NAME = Name
        self.CAREER = Career
        d6 = Dice.Dice(6)
        self.STR = presets[0]
        self.CON = presets[1]
        self.POW = presets[2]
        self.DEX = presets[3]
        self.APP = presets[4]
        self.SIZ = presets[5]
        self.INT = presets[6]
        self.EDU = presets[7]

        self.LUCK = sum(d6.GetBestXOfY(3, 4)) * 5
        self.MAGIC_POINT = int(self.POW / 5)

        self.DamageBonus = 'none'
        dmgAdj = self.STR + self.SIZ
        if dmgAdj >= 0 and dmgAdj <= 64:
            self.DamageBonus = 'subtract 2'
            self.BUILD = -2
        elif dmgAdj >= 65 and dmgAdj <= 84:    
            self.DamageBonus = 'subtract 1'
            self.BUILD = -1
        elif dmgAdj >= 125 and dmgAdj <= 164:    
            self.DamageBonus = 'add 1D4'
            self.BUILD = 1
        elif dmgAdj >= 33 and dmgAdj <= 36:    
            self.DamageBonus = 'add 1D6'
            self.BUILD = 2

        self.HIT_POINT = int((self.CON + self.SIZ) / 10)
        self.SAN = self.POW
        
        self.IDEA = self.INT
        self.KNOW = self.EDU
            
#        self.SANITY_POINT = self.SAN    
#        self.CAREER_SKILL_POINTS = self.EDU * 20
#        self.PERSONAL_INTEREST_SKILL_POINTS = self.INT * 10
#        self.MIN_AGE = self.EDU + 6        
#        self.INCOME = self.calculate_income(d10.Roll())
        self.SKILL_LIST = SkillList(self.DEX, self.EDU)
        self.BACKPACK = InvestigatorBackpack()
        
#    def calculate_income(self, roll):
#        _1890s = [500, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 5000, 10000]
#        _1920s = [1500, 2500, 3500, 3500, 4500, 5500, 6500, 7500, 10000, 20000]
#        _Modern = [15000, 25000, 35000, 45000, 5500, 75000, 100000, 200000, 300000, 500000]
##        if era == Era._1890:
##            return _1890s[roll] 
##        elif era == Era._1920:
#        return _1920s[roll] 
##        elif era == Era._Modern:
##            return _Modern[roll] 
        
    
    def get_stat_format(self, stat, value, half_fifth = None):
        if half_fifth == None:
            return '{0}: {1:-2}'.format(stat, value);
        else:
            return '{0}: {1:-2} {2}'.format(stat, value, half_fifth);

    def print_character_skill(self):
        for key, val in sorted(self.SKILL_LIST.skills.items()):
            print('{0}: {1:-2}'.format(key, val))

    def print_character_backpack(self):
        for val in sorted(self.BACKPACK.items.items()):
            print('{0}'.format(val.name))

    def get_character_sheet(self, ListSkills = True):
        result = ('Investigator: ' + self.NAME + '\n')
        if self.CAREER != '':
            result += (self.CAREER + '\n')
        result += ('\nSTATS:\n')
        result += ('{0}   {1}   {2}\n'.format(self.get_stat_format('STR', self.STR),self.get_stat_format('DEX', self.DEX), self.get_stat_format('POW', self.POW)))
        result += ('{0}   {1}   {2}\n'.format(self.get_stat_format('CON', self.CON),self.get_stat_format('APP', self.APP),self.get_stat_format('EDU', self.EDU)))
        result += ('{0}   {1}   {2}\n'.format(self.get_stat_format('SIZ', self.SIZ),self.get_stat_format('INT', self.INT),''))
        result += ('Damage Modifier: {0}\n'.format(self.DamageBonus))
        result += ('{0}\n'.format(self.get_stat_format('Hit Points',self.HIT_POINT)))
        result += ('{0}\n'.format(self.get_stat_format('Magic Points',self.MAGIC_POINT)))
        result += ('{0}\n'.format(self.get_stat_format('Sanity Points',self.SAN)))
        result += ('{0}\n'.format(self.get_stat_format('Mythos Points',self.MYTHOS_POINTS)))
        if ListSkills == True:
            result += ('\nSKILLS:\n')
            for key, val in sorted(self.SKILL_LIST.skills.items()):
                result += ('{0}: {1:-2}\n'.format(key, val))
        return result
        
    def print_character(self, Hint = False, ListSkills = False, PrintBackpack = False):
        print(self.get_character_sheet(ListSkills))
        if Hint:
            print('{0} {1}'.format('Skill Points (Career)',self.CAREER_SKILL_POINTS))
            print('{0} {1}'.format('Skill Points (Interest)',self.PERSONAL_INTEREST_SKILL_POINTS))
        if PrintBackpack:
            self.BACKPACK.print_backpack()



      
#start_stats = [40, 50, 50, 50, 60, 60, 70, 80]        
#random.shuffle(start_stats)   
##print(start_stats[0]) 
#investgator = Investigator_7_Fast(start_stats)
#investgator.print_character()