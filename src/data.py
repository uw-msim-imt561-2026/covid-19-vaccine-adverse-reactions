## Import Libraries
import pandas as pd
import streamlit as st
from pandas import DataFrame
import kagglehub as kh

## Required cache decorator - needed for streamlit to function
@st.cache_data(show_spinner=False)
def download_datasets() -> str:
    path = kh.dataset_download("ayushggarg/covid19-vaccine-adverse-reactions")
    print("Path to dataset files:", path)
    return path

## Get path to VAERSDATA.csv
def load_vaers(path) -> pd.DataFrame:
    path_to_VAERS = path + "/VAERSDATA.csv"
    df_VAERS = pd.read_csv(path_to_VAERS)
    return df_VAERS

## Import functions from cleaning_VAERS.py
from src.cleaning_VAERS import (handle_whitespace_vaers,
                                handle_numeric_vaers,
                                handle_state_variable,
                                transform_date_cols,
                                transform_yesno_cols,
                                drop_cols_vaers,
                                replace_nulls_w_unknown,
                                handle_date_outliers,
                                handle_non_date_outliers)

## Clean VAERS Dataset
def clean_vaers(df: pd.DataFrame) -> pd.DataFrame:
    df1 = handle_whitespace_vaers(df)
    df2 = handle_numeric_vaers(df1)
    df3 = handle_state_variable(df2)
    df4 = transform_date_cols(df3)
    df5 = transform_yesno_cols(df4)
    df6 = drop_cols_vaers(df5)
    df7 = replace_nulls_w_unknown(df6)
    df8 = handle_date_outliers(df7)
    df9 = handle_non_date_outliers(df8)
    df_vaers_cl = df9
    return df_vaers_cl

## Get path to VAERSVAX.csv
def load_vax(path) -> pd.DataFrame:
    path_to_vax = path + "/VAERSVAX.csv"
    df_vax = pd.read_csv(path_to_vax)
    return df_vax

## Import functions from cleaning_vax.py
from src.cleaning_vax import (handle_whitespace_vax,
                              handle_numeric_vax,
                              handle_categorical_vax,
                              remove_duplicates_vax,
                              handle_outliers_vax)

## Clean VAX dataset
def clean_vax(df: pd.DataFrame) -> pd.DataFrame:
    df1 = handle_whitespace_vax(df)
    df2 = handle_numeric_vax(df1)
    df3 = handle_categorical_vax(df2)
    df4 = remove_duplicates_vax(df3)
    df5 = handle_outliers_vax(df4)
    df_vax_cl = df5
    return df_vax_cl

## Get path to VAERSSYMPTOMS.csv
def load_symptoms(path) -> pd.DataFrame:
    path_to_symptoms = path + "/VAERSSYMPTOMS.csv"
    df_symptoms = pd.read_csv(path_to_symptoms)
    return df_symptoms


## import functions from cleaning_symptoms.py
from src.cleaning_symptoms import (reshape_symptoms, drop_null_symptoms, handle_whitespace_symptoms)

## Clean symptoms dataset
def clean_symptoms(df: pd.DataFrame) -> pd.DataFrame:
    df1 = reshape_symptoms(df)
    df2 = drop_null_symptoms(df1)
    df3 = handle_whitespace_symptoms(df2)
    df_symptoms_cl = df3
    return df_symptoms_cl

def merge_dfs(df_symptoms_cl, df_vaers_cl, df_vax_cl) -> pd.DataFrame:
    """Merge cleaned dataframes from cleaning .py scripts into one dataframe, then filter for only Pfizer and Moderna rows.
    :rtype: pd.DataFrame
    Make sure to call the dataframes in the order specified.
    """
    # merge df_symptoms_cl and df_VAERS_cl
    df_merged_symptoms_VAERS: DataFrame = pd.merge(df_symptoms_cl, df_vaers_cl, how='left', on='VAERS_ID')

    # merge df_vax_cl with previous merge
    df_merged_all = pd.merge(df_merged_symptoms_VAERS, df_vax_cl, how='left', on='VAERS_ID')

    # drop non-Pfizer and non-Moderna rows
    idx_to_drop = df_merged_all[
        (df_merged_all['VAX_MANU'] != 'PFIZER\\BIONTECH') & (df_merged_all['VAX_MANU'] != 'MODERNA')].index
    df_final = df_merged_all.drop(idx_to_drop)

    return df_final
