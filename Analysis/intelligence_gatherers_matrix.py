import numpy as np
import pandas as pd

def get_intelligence_source_matrix(cols):
    ind = ["HUMINT","GEOINT","SIGINT","MASINT","OSINT"]
    df = pd.DataFrame(columns=cols, index=ind)
    return df

def get_game_theory_matrix(choices):
    df = pd.DataFrame(columns=choices, index=choices)
    return df

def get_matrix(columns, indices):
    df = pd.DataFrame(columns=columns, index=indices)
    return df

def set_matrix_value(dataFrame, index, column, value):
    dataFrame.loc[index][column] = value

def get_column_sum(dataFrame, ColumnName):
    return np.nansum(list(dataFrame[ColumnName]))

df_sources = get_intelligence_source_matrix(["Supports Hypothesis", "Does Not Support Hypothesis"])
set_matrix_value(df_sources, "HUMINT", "Does Not Support Hypothesis", True)

print(df_sources)


prisoners_dilema = get_game_theory_matrix(["Confess","Lie"])
set_matrix_value(prisoners_dilema, "Confess", "Confess", "-8,-8")
set_matrix_value(prisoners_dilema, "Confess", "Lie", "0,-10")
set_matrix_value(prisoners_dilema, "Lie", "Confess", "-10,0")
set_matrix_value(prisoners_dilema, "Lie", "Lie", "-1,-1")

print(prisoners_dilema)

decision_matx = get_matrix(["Hybrid","Pick-up","Muscle Car"],["Cost","Practicality","Performance","Reliability","Fuel Economy","Total"])
set_matrix_value(decision_matx,"Cost","Hybrid",3)
set_matrix_value(decision_matx,"Practicality","Hybrid",4)
set_matrix_value(decision_matx,"Performance","Hybrid",4)
set_matrix_value(decision_matx,"Reliability","Hybrid",4)
set_matrix_value(decision_matx,"Fuel Economy","Hybrid",5)
set_matrix_value(decision_matx,"Total","Hybrid",get_column_sum(decision_matx, "Hybrid"))

set_matrix_value(decision_matx,"Cost","Pick-up",5)
set_matrix_value(decision_matx,"Practicality","Pick-up",5)
set_matrix_value(decision_matx,"Performance","Pick-up",3)
set_matrix_value(decision_matx,"Reliability","Pick-up",2)
set_matrix_value(decision_matx,"Fuel Economy","Pick-up",1)
set_matrix_value(decision_matx,"Total","Pick-up",get_column_sum(decision_matx, "Pick-up"))

set_matrix_value(decision_matx,"Cost","Muscle Car",1)
set_matrix_value(decision_matx,"Practicality","Muscle Car",2)
set_matrix_value(decision_matx,"Performance","Muscle Car",5)
set_matrix_value(decision_matx,"Reliability","Muscle Car",3)
set_matrix_value(decision_matx,"Fuel Economy","Muscle Car",1)
set_matrix_value(decision_matx,"Total","Muscle Car",get_column_sum(decision_matx, "Muscle Car"))
print(decision_matx)
