## Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import kagglehub as kh


## Load Data
# Download latest csv version
path = kh.dataset_download("ayushggarg/covid19-vaccine-adverse-reactions")
print("Path to dataset files:", path)

# Create dataframe for df_vax
path_to_vax = path + '/VAERSVAX.csv'
df_vax = pd.read_csv(path_to_vax)


## Handle Whitespace
# remove whitespace at head & tail of string-type columns
for column in df_vax.columns:
    if df_vax[column].dtype == 'str':
        df_vax[column] = df_vax[column].str.strip()

# remove whitespace from any single-word columns
single_word_cols_vax = list(df_vax[['VAX_TYPE','VAX_MANU','VAX_LOT','VAX_DOSE_SERIES','VAX_ROUTE','VAX_SITE']])
for col in single_word_cols_vax:
    if df_vax[col].dtype == 'str':
        df_vax[col] = df_vax[col].str.replace(" ","")


## Handle Numeric Columns
# ensure numeric cols are Int64 or Float type
for column in df_vax.columns:
    if df_vax[column].dtype == 'Int64':
        df_vax[column] = pd.to_numeric(df_vax[column], errors='coerce')
for column in df_vax.columns:
    if df_vax[column].dtype == 'Float':
        df_vax[column] = pd.to_numeric(df_vax[column], errors = 'coerce')


## Categorical Variables - VAX_DOSE_SERIES
# change +7 to just 7
df_vax['VAX_DOSE_SERIES'] = df_vax['VAX_DOSE_SERIES'].replace("7+", "7")

# Convert 'UNK' values to NULL
df_vax['VAX_DOSE_SERIES'] = df_vax['VAX_DOSE_SERIES'].replace("UNK", np.nan)

# convert data type to Int64
df_vax['VAX_DOSE_SERIES'] = df_vax['VAX_DOSE_SERIES'].astype('Int64')


## Categorical Variables - VAX_LOT
# strip remaining whitespace if any
df_vax['VAX_LOT'] = df_vax['VAX_LOT'].str.strip()
df_vax['VAX_LOT'] = df_vax['VAX_LOT'].str.replace(" ", "")

# convert strings to uppercase
df_vax['VAX_LOT'] = df_vax['VAX_LOT'].str.upper()


## Categorical Variables - VAX_ROUTE, VAX_SITE
# replace NULL values with UN for 'Unknown'
df_vax['VAX_ROUTE'] = df_vax['VAX_ROUTE'].replace(np.nan, 'UN')
df_vax['VAX_SITE'] = df_vax['VAX_SITE'].replace(np.nan, 'UN')


## Categorical Variables - VAX_NAME
# simplify vax names
df_vax['VAX_NAME'] = df_vax['VAX_NAME'].str.replace('COVID19 (COVID19 (PFIZER-BIONTECH))', 'PFIZER-BIONTECH')
df_vax['VAX_NAME'] = df_vax['VAX_NAME'].str.replace('COVID19 (COVID19 (UNKNOWN))','Unknown')
df_vax['VAX_NAME'] = df_vax['VAX_NAME'].str.replace('COVID19 (COVID19 (MODERNA))','MODERNA')
df_vax['VAX_NAME'] = df_vax['VAX_NAME'].str.replace('COVID19 (COVID19 (JANSSEN))','JANSSEN')
df_vax['VAX_NAME'] = df_vax['VAX_NAME'].str.replace('COVID19 (COVID19 (MODERNA BIVALENT))','MODERNA BIVALENT')
df_vax['VAX_NAME'] = df_vax['VAX_NAME'].str.replace('COVID19 (COVID19 (PFIZER-BIONTECH BIVALENT))','PFIZER-BIONTECH BIVALENT')
df_vax['VAX_NAME'] = df_vax['VAX_NAME'].str.replace('COVID19 (COVID19 (NOVAVAX))','NOVAVAX')


## Handle Duplicate Rows
# identify wholesale duplicates (where the entire row is the same)
duplicates_vax_df = df_vax[df_vax.duplicated()].sort_values('VAERS_ID')

# drop wholesale duplicates
df_vax = df_vax.drop_duplicates()


## Handle Outliers
# import IQR functions
from cleaning_VAERS import get_iqr_upper, get_iqr_lower, get_iqr_lower_date

# TODO - does it make more sense to get indices and use .drop()?
# create dataframe without Int64 outliers
df_vax = df_vax[df_vax['VAX_DOSE_SERIES']<(get_iqr_upper(df_vax['VAX_DOSE_SERIES']))]


## Save cleaned VAX dataframe to csv (for safekeeping)
path_to_save = path + '/VAERSVAX_cleaned.csv'
df_vax.to_csv(path_to_save)