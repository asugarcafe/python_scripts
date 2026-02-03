# -*- coding: utf-8 -*-

import networkx as nx

#### BEGIN::ENUMS
from enum import Flag, auto # Enum,

class EdgeType(Flag):
    Communication = auto()
    Collaboration = auto()
    SharedTimeSpace = auto()
    
class NodeType(Flag):
    Individual = auto()
    Organization = auto()
    
class OrganizationType(Flag):
    Religious = auto()
    Political = auto()
    Financial = auto()

class SigilType(Flag):
    Email = auto()
    PhoneNumber = auto()
    Moniker = auto()

#### END::ENUMS

#### BEGIN::NODE CLASSES
class Node():
    Type = None
    uuid = None
    Sigils = {}
    
    def __init__(self, UIX = None, NodeType = None):
        self.Type = NodeType
        self.uuid = UIX
        
    
class IndividualNode(Node):
    
    def __init__(self, UUID):
        self.Type = NodeType.Individual
        self.uuid = UUID
        
class OrganizationNode(Node):
    
    def __init__(self, UUID):
        self.Type = NodeType.Organization
        self.uuid = UUID
        
#### END::NODE CLASSES



#### BEGIN::NETWORK CLASSES

class Network():
    NETWORK_BASE = None

    def __init__(self):
        self.NETWORK_BASE = nx.Graph()
        
    def AddEdge(self, Node1, Node2, EdgeTypeEnums):
        self.NETWORK_BASE.add_edge(Node1, Node2, )

#### END::NETWORK CLASSES


network = Network()

donald_trump = IndividualNode()
jeffrey_epstein = IndividualNode()
network.AddEdge(donald_trump, jeffrey_epstein, None)

print(network.NETWORK_BASE.nodes)
nx.draw_networkx(network.NETWORK_BASE)




