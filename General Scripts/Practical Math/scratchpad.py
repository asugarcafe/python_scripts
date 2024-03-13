# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:14:36 2024

@author: sucre
"""

class ElectronicsCalculator():


    @staticmethod
    def calculate_resistance(resistances, connection_type = 'series'):
        if connection_type.lower() == 'series':
            total = sum(resistances)
        elif connection_type.lower() == 'parallel':
            total = 1 / sum(1 / r for r in resistances)
        else:
            raise ValueError("Invalid connection type. Use 'series' or 'parallel'.")
        return total

    @staticmethod
    def calculate_voltage(current, resistance):
        """
        Calculate voltage using Ohm's Law (V = I * R).
        
        Parameters:
            current (float): The electric current in amperes (A).
            resistance (float): The resistance in ohms (Ω).
        
        Returns:
            float: The voltage in volts (V).
        """
        voltage = current * resistance
        return voltage

    @staticmethod
    def calculate_amperage(voltage, resistance):
        """
        Calculate amperage using Ohm's Law (I = V / R).
        
        Parameters:
            voltage (float): The voltage in volts (V).
            resistance (float): The resistance in ohms (Ω).
        
        Returns:
            float: The electric current in amperes (A).
        """
        amperage = voltage / resistance
        return amperage

K = 1000
M = 1000000
resistances = [1670000, 235000]
resistances = [206010.49868766402, 10*K]
typ = 'parallel'
typ = 'series'

print(ElectronicsCalculator.calculate_resistance(resistances, typ))
#666.666,