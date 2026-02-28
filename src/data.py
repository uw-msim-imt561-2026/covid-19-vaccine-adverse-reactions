## Import Libraries
import pandas as pd
import streamlit as st

## Import cleaned dataframes
from cleaning_VAERS import df_VAERS_filtered
from cleaning_vax import df_vax
from cleaning_symptoms import df_symptoms_reshaped

@st.cache_data(show_spinner=False) # this is a decorator --> really need it for streamlit to function effectively
def get_dfs(df1, df2, df3) -> pd.DataFrame:
    df_VAERS_cl = df1
    df_vax_cl = df2
    df_symptoms_cl = df3
    return df_VAERS_cl, df_vax_cl, df_symptoms_cl

def merge_dfs(df1, df2, df3) -> pd.DataFrame:




# from Lab06 -- using to adapt
def load_data(path: str) -> pd.DataFrame:
    '''Loading a small CSV and caching it so the app stays responsive.'''
    df = pd.read_csv(path) # create dataframe
    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
    return df

'''We might create some additional functions/methods in here for data transformations'''
'''Data transformations would take place in THIS file (but cleaning would take place elsewhere, seems like??)'''



#the rest is up to you
# df = df.read_csv(path)
# return df
# check to see if data folder exists. If not create it,
# check to see if clean data.csv exists.
    # if does, so we df = pd.read_csv("data/cean_data.csv")
# if doesn't exist, we check to see if og data files exist
    # if they don't then wedownload from kagglehub, save them to data folder
# process / clean / trasnform data
# write it to  data/clean_data.csv
# df = pd.read_csv("data/clean_Data.csv")