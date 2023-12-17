"""
# this is a two-way frequency table so the rows can be summed to get percentages
                         got anthrax | didnt get anthrax
---------------------------------------------------------                        
ate at facility         |    37      |     33           =   50  total ate there
did not eat at facility |    17      |     13           =   30  total didnt eat there
                                                         -------
                                                            80  total checked
                                                            
#Anthrax matrix as decision event tree
#Ate at Facility    Has Anthrax
#-------------------------------
#                 ┌-----YES (37)
#        YES -----˧
#                 └-----NO  (33)
#
#                 ┌-----YES (17)
#         NO -----˧
#                 └------NO (13)
"""    

'''
# For each YES/NO you should: 
#   1. determine is you have enough evidence, gather more if necessary
#   2. evaluate whther the any evidencew supports this
#
# For each path the evidence supports the final impact should be determined
#
# Final report should show all possible, then likely results with impact
Arms actually on board ship | Arms will reach terrorists | Threat Affect (Impact)
------------------------------------------------------------------------
                                                    ┌---Threat Increases
                             ┌-----YES--------------┼---Threat Unchanged           
                             |                      └---Threat Decreases
        YES -----------------˧                      
                             |                      ┌---Threat Increases
                             └------NO--------------┼---Threat Unchanged            
                                                    └---Threat Decreases


                                                    ┌---Threat Increases
                             ┌-----YES--------------┼---Threat Unchanged
                             |                      └---Threat Decreases
         NO -----------------˧
                             |                      ┌---Threat Increases
                             └------NO--------------┼---Threat Unchanged            
                                                    └---Threat Decreases
'''


import pandas as pd

final_outcomes = ["Threat Increases","Threat Unchanged","Threat Decreases"]
factors = ["Arms actually on board ship","Arms will reach terrorists"]
factor_possibility = ["YES","NO"]

rows_needed = len(factors) * len(factor_possibility)
max_len = max([len(s) for s in factors])
#total_length = sum([len(s) for s in factors]) + (len(factors) + 1) + (max([len(s) for s in final_outcomes]) + 2)

header_cols = ', '.join(factors) + ', Threat Affect '
total_length = len(header_cols)

