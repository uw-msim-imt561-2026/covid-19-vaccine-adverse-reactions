## Import Libraries
import pandas as pd
import streamlit as st
from pandas import DataFrame
import kagglehub as kh


# required cache decorator - needed for streamlit to function
@st.cache_data(show_spinner=False)
def load_data() -> str:
    path = kh.dataset_download("ayushggarg/covid19-vaccine-adverse-reactions")
    print("Path to dataset files:", path)
    return path


def load_vaers(path: str) -> pd.DataFrame:
    path_to_VAERS = path + "/VAERSDATA.csv"
    df_VAERS = pd.read_csv(path_to_VAERS)
    return df_VAERS


# import functions from cleaning_VAERS.py
from src.cleaning_VAERS import (handle_whitespace_vaers,
                                handle_numeric_vaers,
                                handle_state_variable,
                                transform_date_cols,
                                transform_yesno_cols,
                                drop_cols_vaers,
                                replace_nulls_w_unknown,
                                get_iqr_upper,
                                get_iqr_lower,
                                get_iqr_lower_date,
                                handle_date_outliers,
                                handle_non_date_outliers)


def clean_vaers(path: str, df: pd.DataFrame) -> pd.DataFrame:
    handle_whitespace_vaers(df)
    handle_numeric_vaers(df)
    handle_state_variable(df)
    transform_date_cols(df)
    transform_yesno_cols(df)
    drop_cols_vaers(df)
    replace_nulls_w_unknown(df)
    get_iqr_upper(df)
    get_iqr_lower(df)
    get_iqr_lower_date(df)
    handle_date_outliers(df)
    handle_non_date_outliers(df)
    df_vaers_cl = df
    path_to_vaers_cl = path + '/VAERSDATA_cleaned.csv'
    df_vaers_cl.to_csv(path_to_vaers_cl)
    return df_vaers_cl


def load_vax(path: str) -> pd.DataFrame:
    path_to_vax = path + "/VAERSVAX.csv"
    df_vax = pd.read_csv(path_to_vax)
    return df_vax


# import functions from cleaning_vax.py
from src.cleaning_vax import (handle_whitespace_vax,
                              handle_numeric_vax,
                              handle_categorical_vax,
                              remove_duplicates_vax,
                              handle_outliers_vax)


def clean_vax(path: str, df: pd.DataFrame) -> pd.DataFrame:
    handle_whitespace_vax(df)
    handle_numeric_vax(df)
    handle_categorical_vax(df)
    remove_duplicates_vax(df)
    handle_outliers_vax(df)
    df_vax_cl = df
    path_to_vax_cl = path + '/VAERSVAX_cleaned.csv'
    df_vax_cl.to_csv(path_to_vax_cl)
    return df_vax_cl


def load_symptoms(path: str) -> pd.DataFrame:
    path_to_symptoms = path + "/VAERSSYMPTOMS.csv"
    df_symptoms = pd.read_csv(path_to_symptoms)
    return df_symptoms


# import functions from cleaning_symptoms.py
from src.cleaning_symptoms import (reshape_symptoms, drop_null_symptoms, handle_whitespace_symptoms)


def clean_symptoms(path: str, df: pd.DataFrame) -> pd.DataFrame:
    reshape_symptoms(df)
    drop_null_symptoms(df)
    handle_whitespace_symptoms(df)
    df_symptoms_cl = df
    path_to_symptoms_cl = path + '/VAERSVAX_cleaned.csv'
    df_symptoms_cl.to_csv(path_to_symptoms_cl)
    return df_symptoms_cl


def cleaned_vaers_to_csv(path, df: pd.DataFrame) -> pd.DataFrame:
    path_to_vaers = path + "/VAERSDATA_cleaned.csv"
    df.to_csv(path_to_vaers)
    return df


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
