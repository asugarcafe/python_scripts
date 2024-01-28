# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:56:33 2023

@author: sucre
"""

class EnglishSystemBS:
    
    
    @staticmethod
    def MMtoINCH(mm):
        return mm / 25.4

    @staticmethod
    def INCHtoMM(inch):
        return inch * 25.4

class Cylinders:
    
    @staticmethod
    def TwoLiterBottle_DiameterMM():
        return 105
    
    @staticmethod
    def TwoLiterBottle_DiameterINCH():
        return EnglishSystemBS.MMtoINCH(105)
    
    @staticmethod
    def Number2SoupCan_DiameterMM():
        return 87.31
    	
    def Number2SoupCan_HeigthMM():
        return 115.89
    	
    
    #(3 + 7/16) * (4 + 9/16)
    
# print(EnglishSystemBS.INCHtoMM((3 + 7/16)))
# print(EnglishSystemBS.INCHtoMM((4 + 9/16)))