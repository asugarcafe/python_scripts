# https://www.datacamp.com/community/tutorials/social-network-analysis-python
# https://www.nytimes.com/interactive/2018/08/21/us/mueller-trump-charges.html?em_pos=medium&emc=edit_up_20181220&nl=upshot&nl_art=6&nlid=80724309emc%3Dedit_up_20181220&ref=headline&te=1
# https://www.justsecurity.org/trump-russia-timeline/
# https://www.politico.com/interactives/2018/trump-russia-investigation-ties/

import networkx as nx

'''
G_symmetric = nx.Graph()
G_symmetric.add_edge('Amitabh Bachchan','Abhishek Bachchan')
G_symmetric.add_edge('Amitabh Bachchan','Aamir Khan')
G_symmetric.add_edge('Amitabh Bachchan','Akshay Kumar')
G_symmetric.add_edge('Amitabh Bachchan','Dev Anand')
G_symmetric.add_edge('Abhishek Bachchan','Aamir Khan')
G_symmetric.add_edge('Abhishek Bachchan','Akshay Kumar')
G_symmetric.add_edge('Abhishek Bachchan','Dev Anand')
G_symmetric.add_edge('Dev Anand','Aamir Khan')

#nx.draw_networkx(G_symmetric)
#nx.degree(G_symmetric, 'Dev Anand')

G_asymmetric = nx.DiGraph()
G_asymmetric.add_edge('A','B')
G_asymmetric.add_edge('A','D')
G_asymmetric.add_edge('C','A')
G_asymmetric.add_edge('D','E')

nx.spring_layout(G_asymmetric)
nx.draw_networkx(G_asymmetric)

G_weighted = nx.Graph()
G_weighted.add_edge('Amitabh Bachchan','Abhishek Bachchan', weight=99)
G_weighted.add_edge('Amitabh Bachchan','Aaamir Khan', weight=8)
G_weighted.add_edge('Amitabh Bachchan','Akshay Kumar', weight=11)
G_weighted.add_edge('Amitabh Bachchan','Dev Anand', weight=1)
G_weighted.add_edge('Abhishek Bachchan','Aaamir Khan', weight=4)
G_weighted.add_edge('Abhishek Bachchan','Akshay Kumar',weight=7)
G_weighted.add_edge('Abhishek Bachchan','Dev Anand', weight=1)
G_weighted.add_edge('Dev Anand','Aaamir Khan',weight=1)
nx.draw_networkx(G_weighted)
'''


G = nx.MultiGraph()
G.add_edge('A','D',relation ='neighbor')
G.add_edge('A','B',relation='friend')
G.add_edge('A','C',relation='friend')
G.add_edge('B','C', relation='neighbor')
G.add_edge('D','C',relation='friend')
nx.draw_networkx(G)

#MultiEdgeDataView([('A', 'B', {'relation': 'neighbor'}), 
#                   ('A', 'B', {'relation': 'friend'}), 
#                   ('B', 'C', {'relation': 'neighbor'}), 
#                   ('B', 'D', {'relation': 'neighbor'}), 
#                   ('C', 'D', {'relation': 'friend'})])

#G_fb = nx.read_edgelist("facebook_combined.txt", 
#                        create_using = nx.Graph(), 
#                        nodetype=int)
#nx.draw_networkx(G_fb)
