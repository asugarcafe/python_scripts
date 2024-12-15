# -*- coding: utf-8 -*-

import Enums

class Race():
    HideColoring = Enums.RaceColor.Tan
    StartingSocialStatus = Enums.SocialStation.WorkingCasteLow

    def __init__(self):
        '''
        

        Returns
        -------
        None.

        '''

    def SetRace(self, Color = Enums.RaceColor.Tan, Status = Enums.SocialStation.WorkingCasteLow):
        self.HideColoring = Color
        self.StartingSocialStatus = Status