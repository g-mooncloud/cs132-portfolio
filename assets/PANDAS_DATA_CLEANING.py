import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import re
import nltk
import emoji

pio.renderers.default = "notebook"

code_df = pd.read_csv('Codes.csv')
survey_df = pd.read_csv('Dataset.csv')

codeList = code_df["CASEID"].to_list()
codeDesc = code_df["Case Identification"].to_list()
codeDict = dict(zip(codeList, codeDesc))

pd.set_option("future.no_silent_downcasting", True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

survey_df.rename(columns=codeDict, inplace=True)
survey_df.replace(" ", np.nan, inplace=True)
survey_df_removeNullColumns = survey_df.dropna(axis=1, thresh=13911, inplace=False)
survey_df_removeNullRows = survey_df_removeNullColumns.dropna(axis=0, how='any', inplace=False)


irrelevantColumns = ['Country code and phase', 'Cluster number', 'Household number', "Respondent's line number", 'Ultimate area unit', "Women's individual sample weight (6 decimals)", 'Month of interview', 'Year of interview', 'Date of interview (CMC)', 'Date of interview Century Day Code (CDC)', 'Date of birth (CMC)', 'Age in 5-year groups', 'Completeness of age information', 'Result of individual interview', 'Day of interview', 'CMC start of calendar', 'Row of month of interview', 'Length of calendar', 'Number of calendar columns', 'Primary sampling unit', 'Sample strata for sampling errors', 'Stratification used in sample design', 'Number of visits', 'Interviewer identification', 'Field supervisor', 'Line number of husband', 'Cluster altitude in meters', 'Household selected for hemoglobin', 'Selected for Domestic Violence module', 'Team number', 'Team supervisor']
survey_df_cleansed = survey_df_removeNullRows.drop(columns=irrelevantColumns)
survey_df_cleansed = survey_df_cleansed.loc[:,~survey_df_cleansed.columns.duplicated()].copy()

print()
print(survey_df_cleansed.columns)
print()
print(survey_df_cleansed.shape)
