## Import libraries
import pandas as pd
import numpy as np


# class VaxCleaner:
# def __init__(self):

def handle_whitespace_vax(df: pd.DataFrame) -> pd.DataFrame:
    """Removes whitespace from string-type columns in VAERSVAX.csv."""
    for col in df.columns:
        if df[col].dtype == 'str':
            df[col] = df[col].str.strip()
    single_word_cols_vax = list(df_vax[['VAX_TYPE', 'VAX_MANU', 'VAX_LOT', 'VAX_DOSE_SERIES', 'VAX_ROUTE', 'VAX_SITE']])
    for col in single_word_cols_vax:
        if df[col].dtype == 'str':
            df[col] = df[col].str.replace(" ", "")
    return df


def handle_numeric_vax(df: pd.DataFrame) -> pd.DataFrame:
    """Ensures numeric columns in VAERSVAX.csv are either Int64 or Float type."""
    for col in df.columns:
        if df[col].dtype == 'Int64':
            df[col] = pd.to_numeric(df[col], errors='coerce')
    for col in df.columns:
        if df[col].dtype == 'Float':
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def handle_categorical_vax(df: pd.DataFrame) -> pd.DataFrame:
    """Conducts categorical variable transformations for VAERSVAX.csv."""
    # VAX_DOSE_SERIES
    df['VAX_DOSE_SERIES'] = df['VAX_DOSE_SERIES'].replace("7+", "7")
    df['VAX_DOSE_SERIES'] = df['VAX_DOSE_SERIES'].replace("UNK", np.nan)
    df['VAX_DOSE_SERIES'] = df['VAX_DOSE_SERIES'].astype('Int64')

    # VAX_LOT
    df['VAX_LOT'] = df['VAX_LOT'].str.upper()

    # VAX_ROUTE, VAX_SITE
    df['VAX_ROUTE'] = df['VAX_ROUTE'].replace(np.nan, 'UN')
    df['VAX_SITE'] = df['VAX_SITE'].replace(np.nan, 'UN')

    # VAX_NAME
    df['VAX_NAME'] = df['VAX_NAME'].str.replace('COVID19 (COVID19 (PFIZER-BIONTECH))', 'PFIZER-BIONTECH')
    df['VAX_NAME'] = df['VAX_NAME'].str.replace('COVID19 (COVID19 (UNKNOWN))', 'Unknown')
    df['VAX_NAME'] = df['VAX_NAME'].str.replace('COVID19 (COVID19 (MODERNA))', 'MODERNA')
    df['VAX_NAME'] = df['VAX_NAME'].str.replace('COVID19 (COVID19 (JANSSEN))', 'JANSSEN')
    df['VAX_NAME'] = df['VAX_NAME'].str.replace('COVID19 (COVID19 (MODERNA BIVALENT))', 'MODERNA BIVALENT')
    df['VAX_NAME'] = df['VAX_NAME'].str.replace('COVID19 (COVID19 (PFIZER-BIONTECH BIVALENT))',
                                                'PFIZER-BIONTECH BIVALENT')
    df['VAX_NAME'] = df['VAX_NAME'].str.replace('COVID19 (COVID19 (NOVAVAX))', 'NOVAVAX')
    return df


def remove_duplicates_vax(df: pd.DataFrame) -> pd.DataFrame:
    """Drops duplicate rows."""
    df = df.drop_duplicates()
    return df


def handle_outliers_vax(df: pd.DataFrame) -> pd.DataFrame:
    """Removes outliers for VAERSVAX.csv."""
    from cleaning_VAERS import get_iqr_upper
    upper_threshold = get_iqr_upper(df['VAX_DOSE_SERIES'])
    idx_to_drop = (df.index[df['VAX_DOSE_SERIES'] < upper_threshold]).to_list()
    df = df.drop(idx_to_drop)
    # Alternate method if dropping by index has issues: df = df[df['VAX_DOSE_SERIES'] < (get_iqr_upper(df['VAX_DOSE_SERIES']))]
    return df
