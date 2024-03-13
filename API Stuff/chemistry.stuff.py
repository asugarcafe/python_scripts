# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:10:28 2023

@author: sucre
"""
import requests
from chempy import Substance, balance_stoichiometry, mass_fractions
from pprint import pprint



def fetch_periodic_table_data():
    url = "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json"
    response = requests.get(url)
    data = response.json()
    return data

# periodic_table_data = fetch_periodic_table_data()

# # Accessing the data for specific elements
# hydrogen = periodic_table_data["elements"][0]
# helium = periodic_table_data["elements"][1]
# carbon = periodic_table_data["elements"][5]

# Example usage
# print(hydrogen) 
# print(helium)
# print(carbon)


ferricyanide = Substance.from_formula('Fe(CN)6-3')
ferricyanide.composition == {0: -3, 26: 1, 6: 6, 7: 6}  # 0 for charge
#True
print("Unicode Name:" + ferricyanide.unicode_name)
#Fe(CN)₆³⁻
print("Name/HTML: " + ferricyanide.latex_name + ", " + ferricyanide.html_name)
#Fe(CN)_{6}^{3-}, Fe(CN)<sub>6</sub><sup>3-</sup>
print('Mass: %.3f' % ferricyanide.mass + "\r\n")

substances = {s.name: s for s in [
Substance('pancake', composition=dict(eggs=1, spoons_of_flour=2, cups_of_milk=1)),
Substance('eggs_6pack', composition=dict(eggs=6)),
Substance('milk_carton', composition=dict(cups_of_milk=4)),
Substance('flour_bag', composition=dict(spoons_of_flour=60))
]}
pprint([dict(_) for _ in balance_stoichiometry({'eggs_6pack', 'milk_carton', 'flour_bag'},{'pancake'}, substances=substances)])
print('')

reac, prod = balance_stoichiometry({'NH4ClO4', 'Al'}, {'Al2O3', 'HCl', 'H2O', 'N2'})
pprint(dict(reac))
#{'Al': 10, 'NH4ClO4': 6}
pprint(dict(prod))
#{'Al2O3': 5, 'H2O': 9, 'HCl': 6, 'N2': 3}
for fractions in map(mass_fractions, [reac, prod]):
    pprint({k: '{0:.3g} wt%'.format(v*100) for k, v in fractions.items()})