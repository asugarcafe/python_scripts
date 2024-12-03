# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:44:03 2024

@author: sucrerey
"""

import pandas as pd
from enum import Enum

class HML(Enum):
    High = 'High'
    Medium = 'Medium'
    Low = 'Low'
    Unset = 'NULL'


class LikelyHood(Enum):
    HardProof = -1000
    Compelling = -1
    Neutral = 0
    Undefined = 0
    NotApplicable = 0
    Inconsistent = 1
    RulesOut = 1000

class Evidence():
    description = 'CSU found one weapon in neighbors car.'
    credibility = HML.Unset
    relevance = HML.Unset


    def __init__(self, Description = 'Seeing is believing, but evidence is knowing.', hmlRel = HML.Unset, hmlCred = HML.Unset):
        """
        

        Parameters
        ----------
        Description : string, optional
            DESCRIPTION. The default is 'Seeing is believing, but evidence is knowing.'.
        hmlRel : HML, optional
            Clue Relevance. The default is HML.Unset.
        hmlCred : HML, optional
            Clue Credibility. The default is HML.Unset.

        Returns
        -------
        None.

        """
        self.description = Description
        self.relevance = hmlRel
        self.credibility = hmlCred

class EvidenceHypothesisMatrix():
    df = None
    evidence_list = []
    hypothesis_dict = {}
    col_1 = "Evidence Item"

    def __init__(self, EvidenceList, HypothesisDict):
        """
        

        Parameters
        ----------
        EvidenceList : list(Evidence())
            List of Evidence objects.
        HypothesisDict : dict
            Dictionary of hypotheses format: "ShortName":"Longer Description of hypothesis",

        Returns
        -------
        None.

        """
        self.evidence_list = EvidenceList
        self.hypothesis_dict = HypothesisDict

    def update_likelyhood(self, evidenceDesc, colLabel, hml = HML.Unset):

        ind = self.df.index[self.df[self.col_1] == evidenceDesc]
        self.df.at[ind[0], colLabel] = hml


    def build_emptydataframe(self):
        """
        

        Returns
        -------
        pandas DataFrame
            Empty DataFrame with columns defined

        """

        cols = [self.col_1,"Credibility","Relevance"]
        hyp_cols = []
        for label, desc in self.hypothesis_dict.items():
            cols.append(label)
            hyp_cols.append(label)

        self.df = pd.DataFrame(columns = cols)
        for evidence in self.evidence_list:
            new_row = {self.col_1 : evidence.description,
                       "Credibility" : evidence.credibility,
                       "Relevance" : evidence.relevance}
            for hyp in hyp_cols:
                new_row[hyp] = LikelyHood.Undefined

            new_df = pd.DataFrame([new_row])
            self.df = pd.concat([self.df, new_df],ignore_index=True)


    def data_frame(self):
        return self.df


hypotheses = {
    "Neighbor is Killer":"",
    "Coworker is Killer":"",
    "Local Gangster is Killer":"",
    "Spouse is Killer":""
}

evidences = []
evidences.append(Evidence('Victims home was egged a week earlier', HML.High, HML.Medium))
evidences.append(Evidence('Victim had fight with coworker day before.', HML.Medium, HML.High))
evidences.append(Evidence('Victim had drug problem.', HML.Medium, HML.High))
evidences.append(Evidence('Victims spouse has drug problem.', HML.Medium, HML.High))


matrix = EvidenceHypothesisMatrix(evidences, hypotheses)
matrix.build_emptydataframe()
matrix.update_likelyhood(evidences[0].description, "Neighbor is Killer", LikelyHood.RulesOut)
df = matrix.data_frame()


# TODO: Do column counts to find least inconclusive hypotheses
# TODO: this would be bets in a graphical interface, going to hop to other computer to do a prototype Angular project for an hour




"""
"""