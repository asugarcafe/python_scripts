# -*- coding: utf-8 -*-

class Stats():
    Strength = 10
    Dexterity = 10
    Constitution = 10
    Intelligence = 10
    Wisdom = 10
    Charisma = 10

class SinAffinity():
    Pride = 1
    Greed = 1
    Wrath = 1
    Envy = 1
    Lust = 1
    Gluttony = 1
    Sloth = 1


class Character:
    Name = 'Empty Character'
    Stats = None
    SinAffinities = None

    def __init__(self, name):
        """
        

        Returns
        -------
        None.

        """
        self.Name = name
        self.Stats = Stats()
        self.SinAffinities = SinAffinity()


class Dragon(Character):
    Name = 'Standard Dragon'
    Stats = None
    SinAffinities = None

    def __init__(self, name):
        """
        

        Returns
        -------
        None.

        """
        self.Name = name
        self.Stats = Stats()
        self.Stats.Strength = 20
        self.Stats.Dexterity = 20
        self.Stats.Constitution = 20
        self.Stats.Intelligence = 20
        self.Stats.Wisdom = 5
        self.Stats.Charisma = 15

        self.SinAffinities = SinAffinity()
        self.SinAffinities.Pride = 90
        self.SinAffinities.Greed = 90
        self.SinAffinities.Wrath = 90
        self.SinAffinities.Envy = 90
        self.SinAffinities.Lust = 90
        self.SinAffinities.Gluttony = 90
        self.SinAffinities.Sloth = 90