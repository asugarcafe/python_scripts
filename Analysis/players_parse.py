import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pypyodbc as odbc
from scipy.stats import iqr


players = pd.read_csv('players.csv')

distinct_players = players[['fname','lname']]

tags = players['tags']
distinct_tags = set()
for t in tags:
    t_all = t.split(' ')
    for a in t_all:
        distinct_tags.add(a.replace("'","").replace("}",""))

distinct_tags.remove('{class:')
distinct_tags.remove('g-list-item')
#print(distinct_tags)        


associations = players['associations']
distinct_associations = set()
for ass in associations:
    t_ass = ass.split(",")
    for a in t_ass:
        distinct_associations.add(a.strip())
        
#print(distinct_associations)        


subplots = players['subplots']
distinct_subplots = set()
for sub in subplots:
    s = str(sub)
    if s.find(",") == -1:
        distinct_subplots.add(s.strip())
    else:
        t_sub = s.split(",")
        for a in t_sub:
            distinct_subplots.add(a.strip())

distinct_subplots.remove('nan')
#print(distinct_subplots)        

links = []
#Emin	Agalarov
links.append((1,0,"father-son"))
links.append((0,292,""))
print(links)

players_stolen_email = players.loc[players["subplots"].str.contains('Stolen emails',na=False)]
players_fake_news = players.loc[players["subplots"].str.contains('Fake news',na=False)]
players_ira = players.loc[players["associations"].str.contains('Internet Research Agency',na=False)]
players_indicted = players.loc[players["tags"].str.contains('Indicted',na=False)]
players_steele_dossier = players.loc[players["tags"].str.contains('TheSteeledossier',na=False)]


