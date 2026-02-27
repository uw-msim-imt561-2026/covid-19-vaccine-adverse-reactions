## Import Libraries
import pandas as pd
import numpy as np
import kagglehub as kh


## Load Data
# download datasets (latest .csv files from Kaggle)
path = kh.dataset_download("ayushggarg/covid19-vaccine-adverse-reactions")
print("Path to dataset files:", path)

# create symptoms dataframe
path_to_symptoms = path + '/VAERSSYMPTOMS.csv'
df_symptoms = pd.read_csv(path_to_symptoms)
df_symptoms.head()


## Reshape Symptoms Dataset
# convert SYMPTOM / SYMPTOMVERSION pairs to dictionary item in series
VAERS_IDs_dict = df_symptoms[['VAERS_ID']].apply(lambda row: row.to_dict(), axis=1)
symptom1_dict = df_symptoms[['SYMPTOM1','SYMPTOMVERSION1']].apply(lambda row: row.to_dict(), axis=1)
symptom2_dict = df_symptoms[['SYMPTOM2','SYMPTOMVERSION2']].apply(lambda row: row.to_dict(), axis=1)
symptom3_dict = df_symptoms[['SYMPTOM3','SYMPTOMVERSION3']].apply(lambda row: row.to_dict(), axis=1)
symptom4_dict = df_symptoms[['SYMPTOM4','SYMPTOMVERSION4']].apply(lambda row: row.to_dict(), axis=1)
symptom5_dict = df_symptoms[['SYMPTOM5','SYMPTOMVERSION5']].apply(lambda row: row.to_dict(), axis=1)

# create subset dataset of VAERS_IDs
df_VAERS_IDs = df_symptoms['VAERS_ID'].to_frame()

# convert symptom1_dict through symptom5_dict to dataframe
symptom1_df = symptom1_dict.to_frame()
symptom2_df = symptom2_dict.to_frame()
symptom3_df = symptom3_dict.to_frame()
symptom4_df = symptom4_dict.to_frame()
symptom5_df = symptom5_dict.to_frame()

# add column with VAERS_ID values to new dataframes
symptom1_df['VAERS_ID'] = df_VAERS_IDs
symptom2_df['VAERS_ID'] = df_VAERS_IDs
symptom3_df['VAERS_ID'] = df_VAERS_IDs
symptom4_df['VAERS_ID'] = df_VAERS_IDs
symptom5_df['VAERS_ID'] = df_VAERS_IDs

# add columns for 'symptom' and 'symptom version' to each frame
symptom1_df['symptom'] = symptom1_df[0].apply(lambda row: row['SYMPTOM1'])
symptom1_df['symptom version'] = symptom1_df[0].apply(lambda row: row['SYMPTOMVERSION1'])

symptom2_df['symptom'] = symptom2_df[0].apply(lambda row: row['SYMPTOM2'])
symptom2_df['symptom version'] = symptom2_df[0].apply(lambda row: row['SYMPTOMVERSION2'])

symptom3_df['symptom'] = symptom3_df[0].apply(lambda row: row['SYMPTOM3'])
symptom3_df['symptom version'] = symptom3_df[0].apply(lambda row: row['SYMPTOMVERSION3'])

symptom4_df['symptom'] = symptom4_df[0].apply(lambda row: row['SYMPTOM4'])
symptom4_df['symptom version'] = symptom4_df[0].apply(lambda row: row['SYMPTOMVERSION4'])

symptom5_df['symptom'] = symptom5_df[0].apply(lambda row: row['SYMPTOM5'])
symptom5_df['symptom version'] = symptom5_df[0].apply(lambda row: row['SYMPTOMVERSION5'])

# concatenate all dataframes into one + reorder cols
symptom_dataframes = [symptom1_df, symptom2_df, symptom3_df, symptom4_df, symptom5_df]
df_symptoms_reshaped = pd.concat(symptom_dataframes)
df_symptoms_reshaped = df_symptoms_reshaped.iloc[:, [1, 2, 3, 0]]

# rename dictionary column for reference
df_symptoms_reshaped = df_symptoms_reshaped.set_axis(['VAERS_ID', 'symptom', 'symptom_version', 'symptom_dict'], axis=1)


## Drop NA Values
df_symptoms_reshaped = df_symptoms_reshaped.dropna()

## Remove Whitespace from string cols
df_symptoms_reshaped['symptom'] = df_symptoms_reshaped['symptom'].str.strip()


## Save transformed symptoms dataframe to csv
path_to_save = path + '/VAERSSYMPTOMS_cleaned.csv'
df_symptoms_reshaped.to_csv(path_to_save)