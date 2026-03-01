## Import libraries
import pandas as pd
import numpy as np

def handle_whitespace_vaers(df) -> pd.DataFrame:
    """Removes whitespace from string-type columns."""
    for col in df.columns:
        if df[col].dtype == 'str':
            df[col] = df[col].str.strip()
    single_word_cols = list(df[['RECVDATE', 'STATE', 'RPT_DATE', 'DIED', 'DATEDIED', 'L_THREAT', 'ER_VISIT',
                                  'HOSPITAL', 'X_STAY', 'DISABLE', 'BIRTH_DEFECT', 'RECOVD', 'VAX_DATE',
                                  'ONSET_DATE', 'V_ADMINBY', 'V_FUNDBY']])
    for col in single_word_cols:
        df[col] = df[col].str.replace(" ", "")
    return df

def handle_numeric_vaers(df) -> pd.DataFrame:
    """Ensures numeric columns are Int64 or Float type."""
    for col in df.columns:
        if df[col].dtype == 'int64':
            df[col] = df[col].astype('Int64')
    for col in df.columns:
        if df[col].dtype == 'Float':
            df[col] = df[col].astype('Float')
    return df

def handle_state_variable(df) -> pd.DataFrame:
    """Addresses typos in 'STATE' column."""
    # get unique STATE values
    unique_STATE = list(df['STATE'].unique())
    # remove non-str values
    for item in unique_STATE:
        if type(item) != str:
            unique_STATE.remove(item)
    unique_STATE = sorted(unique_STATE)
    # fix issues in STATE column
    df['STATE'] = df['STATE'].replace('Tx','TX')
    df['STATE'] = df['STATE'].replace('Ca','CA')
    # replacing remaining STATE typos
    df['STATE'] = df['STATE'].replace(['FM', 'MH', 'PW', 'QM', 'QW', 'XB', 'XL', 'XV'], np.nan)
    return df

def transform_date_cols(df) -> pd.DataFrame:
    """Converts date columns to datetime objects and adds Year, Month, and MonthYear columns to dataframe."""
    # convert date columns to datetime objects
    df['RECVDATE'] = df['RECVDATE'].astype('datetime64[ns]')
    df['DATEDIED'] = df['DATEDIED'].astype('datetime64[ns]')
    df['VAX_DATE'] = df['VAX_DATE'].astype('datetime64[ns]')
    df['ONSET_DATE'] = df['ONSET_DATE'].astype('datetime64[ns]')
    df['TODAYS_DATE'] = df['TODAYS_DATE'].astype('datetime64[ns]')
    df['RPT_DATE'] = df['RPT_DATE'].astype('datetime64[ns]')
    # add Year, Month, and MonthYear columns
    df['ONSET_YEAR'] = df['ONSET_DATE'].dt.year
    df['ONSET_MONTH'] = df['ONSET_DATE'].dt.strftime('%b')
    df['ONSET_MONTHYEAR'] = df['ONSET_DATE'].dt.strftime('%Y-%m')
    return df

def transform_yesno_cols(df) -> pd.DataFrame:
    """Changes null values in yes/no string cols to 'N'."""
    # change nan values to 'N' in yes/no string columns
    df['DIED'] = df['DIED'].replace(np.nan, 'N')
    df['L_THREAT'] = df['L_THREAT'].replace(np.nan, 'N')
    df['ER_VISIT'] = df['ER_VISIT'].replace(np.nan, 'N')
    df['HOSPITAL'] = df['HOSPITAL'].replace(np.nan, 'N')
    df['X_STAY'] = df['X_STAY'].replace(np.nan, 'N')
    df['DISABLE'] = df['DISABLE'].replace(np.nan, 'N')
    df['BIRTH_DEFECT'] = df['BIRTH_DEFECT'].replace(np.nan, 'N')
    df['OFC_VISIT'] = df['OFC_VISIT'].replace(np.nan, 'N')
    df['ER_ED_VISIT'] = df['ER_ED_VISIT'].replace(np.nan, 'N')
    return df

def drop_cols_vaers(df) -> pd.DataFrame:
    """Drops unnecessary columns from VAERS csv."""
    df_filtered = df.drop(['CAGE_YR', 'CAGE_MO', 'SYMPTOM_TEXT', 'LAB_DATA', 'OTHER_MEDS', 'CUR_ILL', 'HISTORY', 'PRIOR_VAX', 'SPLTTYPE',
         'ALLERGIES'], axis=1)
    return df_filtered

def replace_nulls_w_unknown(df) -> pd.DataFrame:
    """Replaces null values with 'UNK' or 'U' for Unknown in 'RECOVD', 'V_ADMINBY', 'V_FUNDBY'."""
    # Keeping as string, specific cleaning instructions regarding NULLS provided by data dictionary
    df.fillna({'RECOVD': "U"},
                             inplace=True)  # Data of unknown status of vaccine recovery is in column already. Just replacing NULLS with "U"
    df.fillna({'V_ADMINBY': "UNK"},
                             inplace=True)  # Location of administration specifies an "Unknown" observation. Just replacing NULLS with "UNK"
    df.fillna({'V_FUNDBY': "UNK"},
                             inplace=True)  # Specifies that purchase history can be Other/Unknown. Just replacing NULLS with "UNK"
    return df

# IQR Functions for Outliers
def get_iqr_upper(x):
    """Returns upper threshold of interquartile range."""
    return x.quantile(0.75)+(1.5*(x.quantile(0.75)-x.quantile(0.25)))

def get_iqr_lower(x):
    """Returns lower threshold of interquartile range."""
    iqr_low = x.quantile(0.25)-(1.5*(x.quantile(0.75)-x.quantile(0.25)))
    if iqr_low < 0:
        return 0
    else:
        return iqr_low

def get_iqr_lower_date(x):
    """Returns lower threshold of interquartile range for date columns."""
    return x.quantile(0.25)-(1.5*(x.quantile(0.75)-x.quantile(0.25)))

def handle_date_outliers(df) -> pd.DataFrame:
    """Removes date outliers."""
    # set lower date limit
    from datetime import datetime as dt
    lower_date_str = '2020-01-01'
    lower_date_limit = dt.strptime(lower_date_str, '%Y-%m-%d')

    # set upper date limit
    upper_date_str = '2025-12-31'
    upper_date_limit = dt.strptime(upper_date_str, '%Y-%m-%d')

    # get indices of rows to drop
    index_dates_above_2025 = (df.index[df['ONSET_DATE'].dt.year > 2025]).to_list()
    index_dates_ONSET = (df.index[df['ONSET_DATE'].dt.year < 2020]).tolist()
    index_dates_VAX = (df.index[df['VAX_DATE'].dt.year < 2020]).tolist()
    index_dates_TODAY = (df.index[df['TODAYS_DATE'].dt.year < 2020]).tolist()
    index_dates_DIED = (df.index[df['DATEDIED'].dt.year < 2020]).tolist()
    index_dates_below_2020 = index_dates_ONSET + index_dates_VAX + index_dates_TODAY + index_dates_DIED

    # drop dates after 2025
    df = df.drop(index_dates_above_2025)

    # drop dates before 2020
    df = df.drop(index_dates_below_2020)
    return df

def handle_non_date_outliers(df) -> pd.DataFrame:
    """Removes non-date outliers."""
    # get upper & lower values for outliers
    upper_AGE = get_iqr_upper(df['AGE_YRS'])
    lower_AGE = get_iqr_lower(df['AGE_YRS'])
    upper_HOSPDAYS = get_iqr_upper(df['HOSPDAYS'])
    lower_HOSPDAYS = get_iqr_lower(df['HOSPDAYS'])
    upper_NUMDAYS = get_iqr_upper(df['NUMDAYS'])
    lower_NUMDAYS = get_iqr_lower(df['NUMDAYS'])

    # get indices of rows to drop
    index_AGE_YRS_upper = (df.index[df['AGE_YRS'] > upper_AGE]).tolist()
    index_AGE_YRS_lower = (df.index[df['AGE_YRS'] < lower_AGE]).tolist()
    index_HOSPDAYS_upper = (df.index[df['HOSPDAYS'] > upper_HOSPDAYS]).tolist()
    index_HOSPDAYS_lower = (df.index[df['HOSPDAYS'] < lower_HOSPDAYS]).tolist()
    index_NUMDAYS_upper = (df.index[df['NUMDAYS'] > upper_NUMDAYS]).tolist()
    index_NUMDAYS_lower = (df.index[df['NUMDAYS'] < lower_NUMDAYS]).tolist()
    index_rows_to_drop = index_AGE_YRS_upper + index_AGE_YRS_lower + index_HOSPDAYS_upper + index_HOSPDAYS_lower + index_NUMDAYS_upper + index_NUMDAYS_lower

    # drop rows
    df = df.drop(index_rows_to_drop)
    return df

# TODO - Remove if we're not going to make this a class, OR frame around functions above
# class VAERSCleaner:
    # def __init__(self) -> pd.DataFrame: