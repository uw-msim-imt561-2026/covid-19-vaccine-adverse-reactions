## Import libraries
import pandas as pd
import numpy as np
import kagglehub as kh


## Load Data
# download datasets (latest .csv files from Kaggle)
path = kh.dataset_download("ayushggarg/covid19-vaccine-adverse-reactions")
print("Path to dataset files:", path)

# create dataframe for df_VAERS
path_to_VAERS = path + '/VAERSDATA.csv'
df_VAERS = pd.read_csv(path_to_VAERS)


## Handle Whitespace
# remove whitespace at head & tail of str-type columns
for column in df_VAERS.columns:
    if df_VAERS[column].dtype == 'str':
        df_VAERS[column] = df_VAERS[column].str.strip()

# remove whitespace from single-word str columns
single_word_cols_VAERS = list(df_VAERS[['REVALIDATE','STATE','RPT_DATE','DIED','DATEDIED','L_THREAT','ER_VISIT','HOSPITAL','X_STAY','DISABLE','BIRTH_DEFECT','RECOVD','VAX_DATE','ONSET_DATE','V_ADMINBY','V_FUNDBY']])
for col in single_word_cols_VAERS:
    df_VAERS[col] = df_VAERS[col].str.replace(" ","")


## Handle Numeric Columns
# ensure numeric cols are Int64 or Float type
for column in df_VAERS.columns:
    if df_VAERS[column].dtype == 'int64':
        df_VAERS[column] = df_VAERS[column].astype('Int64')
for column in df_VAERS.columns:
    if df_VAERS[column].dtype == 'Float':
        df_VAERS[column] = df_VAERS[column].astype('Float')


## Handle Categorical Variables
# get unique values for relevant columns
unique_STATE = list(df_VAERS['STATE'].unique())
unique_SEX = list(df_VAERS['SEX'].unique())
unique_V_ADMINBY = list(df_VAERS['V_ADMINBY'].unique())
unique_V_FUNDBY = list(df_VAERS['V_FUNDBY'].unique())
unique_RECOVD = list(df_VAERS['RECOVD'].unique())
unique_FORM_VERS = list(df_VAERS['FORM_VERS'].unique())

# unique_STATE - remove non-str values
for item in unique_STATE:
    if type(item) != str:
        unique_STATE.remove(item)
unique_STATE = sorted(unique_STATE)

# fix issues in STATE column
df_VAERS['STATE'] = df_VAERS['STATE'].replace('Tx','TX')
df_VAERS['STATE'] = df_VAERS['STATE'].replace('Ca','CA')

# replacing remaining STATE typos
df_VAERS['STATE'] = df_VAERS['STATE'].replace(['FM', 'MH', 'PW', 'QM', 'QW', 'XB', 'XL', 'XV'], np.nan)


## Transform Date Columns
# convert date columns to datetime objects
df_VAERS['RECVDATE'] = df_VAERS['RECVDATE'].astype('datetime64[ns]')
df_VAERS['DATEDIED'] = df_VAERS['DATEDIED'].astype('datetime64[ns]')
df_VAERS['VAX_DATE'] = df_VAERS['VAX_DATE'].astype('datetime64[ns]')
df_VAERS['ONSET_DATE'] = df_VAERS['ONSET_DATE'].astype('datetime64[ns]')
df_VAERS['TODAYS_DATE'] = df_VAERS['TODAYS_DATE'].astype('datetime64[ns]')
df_VAERS['RPT_DATE'] = df_VAERS['RPT_DATE'].astype('datetime64[ns]')

# add Year, Month, and MonthYear columns
df_VAERS['ONSET_YEAR'] = df_VAERS['ONSET_DATE'].dt.year
df_VAERS['ONSET_MONTH'] = df_VAERS['ONSET_DATE'].dt.strftime('%b')
df_VAERS['ONSET_MONTHYEAR'] = df_VAERS['ONSET_DATE'].dt.strftime('%Y-%m')
df_VAERS.head()


## Transform Y/N String Columns
# change nan values to 'N' in boolean columns (string data type with binary values)
df_VAERS['DIED'] = df_VAERS['DIED'].replace(np.nan,'N')
df_VAERS['L_THREAT'] = df_VAERS['L_THREAT'].replace(np.nan,'N')
df_VAERS['ER_VISIT'] = df_VAERS['ER_VISIT'].replace(np.nan,'N')
df_VAERS['HOSPITAL'] = df_VAERS['HOSPITAL'].replace(np.nan,'N')
df_VAERS['X_STAY'] = df_VAERS['X_STAY'].replace(np.nan,'N')
df_VAERS['DISABLE'] = df_VAERS['DISABLE'].replace(np.nan,'N')
df_VAERS['BIRTH_DEFECT'] = df_VAERS['BIRTH_DEFECT'].replace(np.nan,'N')
df_VAERS['OFC_VISIT'] = df_VAERS['OFC_VISIT'].replace(np.nan,'N')
df_VAERS['ER_ED_VISIT'] = df_VAERS['ER_ED_VISIT'].replace(np.nan,'N')


## Drop Unnecessary Columns
df_VAERS_filtered = df_VAERS.drop(['CAGE_YR', 'CAGE_MO', 'SYMPTOM_TEXT', 'LAB_DATA', 'OTHER_MEDS', 'CUR_ILL', 'HISTORY', 'PRIOR_VAX', 'SPLTTYPE', 'ALLERGIES'], axis=1)

## Replace null values with "UNK" ("Unknown") in 'RECOVD', 'V_ADMINBY', 'V_FUNDBY'
# Keeping as string, specific cleaning instructions regarding NULLS provided by data dictionary
df_VAERS_filtered.fillna({'RECOVD':"U"}, inplace = True) # Data of unknown status of vaccine recovery is in column already. Just replacing NULLS with "U"
df_VAERS_filtered.fillna({'V_ADMINBY':"UNK"}, inplace = True) # Location of administration specifies an "Unknown" observation. Just replacing NULLS with "UNK"
df_VAERS_filtered.fillna({'V_FUNDBY':"UNK"}, inplace = True) # Specifies that purchase history can be Other/Unknown. Just replacing NULLS with "UNK"


## Write IQR Functions for Outliers
def get_iqr_upper(x):
    return x.quantile(0.75)+(1.5*(x.quantile(0.75)-x.quantile(0.25)))

def get_iqr_lower(x):
    iqr_low = x.quantile(0.25)-(1.5*(x.quantile(0.75)-x.quantile(0.25)))
    if iqr_low < 0:
        return 0
    else:
        return iqr_low

# adding lower range function for date handling
def get_iqr_lower_date(x):
    return x.quantile(0.25)-(1.5*(x.quantile(0.75)-x.quantile(0.25)))


## Handle Date Outliers
# set lower date limit
from datetime import datetime as dt
lower_date_str = '2020-01-01'
lower_date_limit = dt.strptime(lower_date_str, '%Y-%m-%d')

# set upper date limit
upper_date_str = '2025-12-31'
upper_date_limit = dt.strptime(upper_date_str, '%Y-%m-%d')

# get indices of rows to drop
index_dates_above_2025 = (df_VAERS_filtered.index[df_VAERS_filtered['ONSET_DATE'].dt.year > 2025]).to_list()
index_dates_ONSET = (df_VAERS_filtered.index[df_VAERS_filtered['ONSET_DATE'].dt.year < 2020]).tolist()
index_dates_VAX = (df_VAERS_filtered.index[df_VAERS_filtered['VAX_DATE'].dt.year < 2020]).tolist()
index_dates_TODAY = (df_VAERS_filtered.index[df_VAERS_filtered['TODAYS_DATE'].dt.year < 2020]).tolist()
index_dates_DIED = (df_VAERS_filtered.index[df_VAERS_filtered['DATEDIED'].dt.year < 2020]).tolist()
index_dates_below_2020 = index_dates_ONSET + index_dates_VAX + index_dates_TODAY + index_dates_DIED

# drop dates after 2025
df_VAERS_filtered = df_VAERS_filtered.drop(index_dates_above_2025)

# drop dates before 2020
df_VAERS_filtered = df_VAERS_filtered.drop(index_dates_below_2020)


## Handle Non-Date Outliers
# get upper & lower values for outliers
upper_AGE = get_iqr_upper(df_VAERS_filtered['AGE_YRS'])
lower_AGE = get_iqr_lower(df_VAERS_filtered['AGE_YRS'])
upper_HOSPDAYS = get_iqr_upper(df_VAERS_filtered['HOSPDAYS'])
lower_HOSPDAYS = get_iqr_lower(df_VAERS_filtered['HOSPDAYS'])
upper_NUMDAYS = get_iqr_upper(df_VAERS_filtered['NUMDAYS'])
lower_NUMDAYS = get_iqr_lower(df_VAERS_filtered['NUMDAYS'])

# get indices of rows to drop
index_AGE_YRS_upper = (df_VAERS_filtered.index[df_VAERS_filtered['AGE_YRS'] > upper_AGE]).tolist()
index_AGE_YRS_lower = (df_VAERS_filtered.index[df_VAERS_filtered['AGE_YRS'] < lower_AGE]).tolist()
index_HOSPDAYS_upper = (df_VAERS_filtered.index[df_VAERS_filtered['HOSPDAYS'] > upper_HOSPDAYS]).tolist()
index_HOSPDAYS_lower = (df_VAERS_filtered.index[df_VAERS_filtered['HOSPDAYS'] < lower_HOSPDAYS]).tolist()
index_NUMDAYS_upper = (df_VAERS_filtered.index[df_VAERS_filtered['NUMDAYS'] > upper_NUMDAYS]).tolist()
index_NUMDAYS_lower = (df_VAERS_filtered.index[df_VAERS_filtered['NUMDAYS'] < lower_NUMDAYS]).tolist()
index_rows_to_drop = index_AGE_YRS_upper + index_AGE_YRS_lower + index_HOSPDAYS_upper + index_HOSPDAYS_lower + index_NUMDAYS_upper + index_NUMDAYS_lower

# drop rows
df_VAERS_filtered = df_VAERS_filtered.drop(index_rows_to_drop)


## Save cleaned VAERS dataframe to csv (for safekeeping)
path_to_save = path + '/VAERSDATA_cleaned.csv'
df_VAERS_filtered.to_csv(path_to_save)