## Import Libraries
import pandas as pd
import streamlit as st
from pandas import DataFrame
import kagglehub as kh

# required cache decorator - needed for streamlit to function
@st.cache_data(show_spinner=False)
def load_data() -> DataFrame:
    # download datasets (latest .csv files from Kaggle)
    path = kh.dataset_download("ayushggarg/covid19-vaccine-adverse-reactions")
    print("Path to dataset files:", path)

    # get paths to csv files
    path_to_VAERS = path + "/VAERSDATA.csv"
    path_to_vax = path + "/VAERSVAX.csv"
    path_to_symptoms = path + "/VAERSSYMPTOMS.csv"

    # write CSVs to dataframes
    df_VAERS = pd.read_csv(path_to_VAERS)
    df_vax = pd.read_csv(path_to_vax)
    df_symptoms = pd.read_csv(path_to_symptoms)

    return df_VAERS, df_vax, df_symptoms

# TODO - Put in functions from cleaning scripts
# CLEAN VAERS DATA (PUT IN FUNCTIONS)

# CLEAN VAX DATA (PUT IN FUNCTIONS)

# CLEAN SYMPTOMS DATA (PUT IN FUNCTIONS)

def merge_dfs() -> pd.DataFrame:
    """Merge cleaned dataframes from cleaning .py scripts into one dataframe, then filter for only Pfizer and Moderna rows.
    :rtype: pd.DataFrame
    """
    # import dataframes from cleaned scripts
    from cleaning_VAERS import df_VAERS_filtered
    from cleaning_vax import df_vax
    from cleaning_symptoms import df_symptoms_reshaped

    # merge df_symptoms_cl and df_VAERS_cl
    df_merged_symptoms_VAERS: DataFrame = pd.merge(df_symptoms_reshaped, df_VAERS_filtered, how='left', on='VAERS_ID')

    # merge df_vax_cl with previous merge
    df_merged_all = pd.merge(df_merged_symptoms_VAERS, df_vax, how='left', on='VAERS_ID')

    # drop non-Pfizer and non-Moderna rows
    idx_to_drop = df_merged_all[
        (df_merged_all['VAX_MANU'] != 'PFIZER\\BIONTECH') & (df_merged_all['VAX_MANU'] != 'MODERNA')].index
    df = df_merged_all.drop(idx_to_drop)

    return df

# def save_cleaned_df(df) -> pd.DataFrame:

## Save cleaned VAERS dataframe to csv (for safekeeping)
# path_to_save = path + '/VAERSDATA_cleaned.csv'
# df_VAERS_filtered.to_csv(path_to_save)