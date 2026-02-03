# -*- coding: utf-8 -*-

#### BEGIN::ENUMS
from enum import Enum, Flag, auto

class EdgeType(Flag):
    Individual = auto()
    Organization = auto()
    
class NodeType(Flag):
    Individual = auto()
    Organization = auto()
    
class OrganizationType(Flag):
    Religious = auto()
    Political = auto()
    Financial = auto()

#### END::ENUMS

#### BEGIN::NODE CLASSES
class Node():
    Type = None
    
    def __init__(self, NodeType = None):
        self.Type = NodeType

class IndividualNode(Node):
    
    def __init__(self):
        self.Type = NodeType.Individual
        
class OrganizationNode(Node):
    
    def __init__(self):
        self.Type = NodeType.Organization
        
        
#### END::NODE CLASSES
        