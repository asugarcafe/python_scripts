# -*- coding: utf-8 -*-

import uuid
import json
from collections import OrderedDict
#uuid.uuid4()

class Actor:
    Id = ""
    Name = ""
    Organizations = []
    Motives = []

    def __init__(self, name, identifier = None):
        """
        

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        identifier : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """
        self.Name = name
        if identifier == None:
            self.Id = str(uuid.uuid4())
        else:
            self.Id = identifier

        self.Organizations = []
        self.Motives = []

class Organization:
    Id = ""
    Name = ""

    def __init__(self, name, identifier = None):
        """
        

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        identifier : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """
        self.Name = name
        if identifier == None:
            self.Id = str(uuid.uuid4())
        else:
            self.Id = identifier


actors = [Actor("Ann Archer"),
     Actor("Bobby Bonilla"),
     Actor("Charlie Chapman")]
print([a.__dict__ for a in actors ])
js = json.dumps([a.__dict__ for a in actors ])





"""
"""