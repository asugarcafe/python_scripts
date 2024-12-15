# -*- coding: utf-8 -*-

from enum import Enum

class SocialStation(Enum):
    RulingCaste = 1
    ReligiousCaste = 2
    WorkingCasteHigh = 3
    WorkingCasteLow = 4
    Immigrant = 5
    Slave = 6
    Outcast = 7

class RaceColor(Enum):
    UltraRich = 0
    Invisible = 1
    PaleWhite = 2
    TanWhite = 3
    Tan = 4
    Brown = 5
    Black = 6
    
class Gender(Enum):
    Male = 1
    Female = 2
    Asexual = 3
    Hermaphrodite = 4
    TransMale = 5
    TransFemale = 6
    AlienGenders = 7

class OccupationTemplate(Enum):
    Dragon = 0
    CEO = 1
    Governor = 2
    Politician = 3
    Lawyer = 4
    Constable = 5
    Techworker = 8
    Tradeworker = 9
    UnskilledWorker = 10
    Slave = 11
    Unemployed = 12