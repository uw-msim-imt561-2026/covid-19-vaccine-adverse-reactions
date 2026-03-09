## Import Libraries
import pandas as pd
import streamlit as st

## Required cache decorator - needed for streamlit to function
@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
    df = pd.read_csv('data/west_states_filtered_v2.csv')
    df['ONSET_DATE'] = df['ONSET_DATE'].astype('datetime64[ns]')
    df['TODAYS_DATE'] = df['TODAYS_DATE'].astype('datetime64[ns]')
    df['SEX'] = df['SEX'].replace('F', 'Female')
    df['SEX'] = df['SEX'].replace('M', 'Male')
    df['SEX'] = df['SEX'].replace('U', 'Unknown or Undisclosed')
    df['ONSET_YEAR'] = df['ONSET_DATE'].dt.year
    df['MONTH_YEAR'] = df['ONSET_DATE'].dt.strftime('%Y-%m')
    #df = df.drop('Unnamed: 0', axis=1)
    return df

## Calculate KPI metrics
def get_total_events_kpi(df: pd.DataFrame) -> str:
    """Calculates the total sum of VAERS reports in a given span of time (already filtered in the dataframe arg)."""
    df_kpi_grouped = (df.groupby(by=["MONTH_YEAR"]).agg(report_count=("VAERS_ID", "count"))).reset_index()
    total_reports = df_kpi_grouped['report_count'].sum()
    total_reports_str = str(total_reports)
    return total_reports_str

def get_total_hosp_kpi(df: pd.DataFrame) -> str:
    """Calculates the total sum of VAERS reports in a given span of time (already filtered in the dataframe arg), in which the patient was hospitalized."""
    df_hosp = df[df['HOSPITAL'] == 'Y']
    df_kpi_hosp = (df_hosp.groupby(by=["MONTH_YEAR"]).agg(report_count=("VAERS_ID", "count"))).reset_index()
    total_hosp = df_kpi_hosp['report_count'].sum()
    total_hosp_str = str(total_hosp)
    return total_hosp_str

def get_total_died_kpi(df: pd.DataFrame) -> str:
    """Calculates the total sum of VAERS reports in a given span of time (already filtered in the dataframe arg), in which the patient died."""
    df_died = df[df['DIED'] == 'Y']
    df_kpi_died = (df_died.groupby(by=["MONTH_YEAR"]).agg(report_count=("VAERS_ID", "count"))).reset_index()
    total_died = df_kpi_died['report_count'].sum()
    total_died_str = str(total_died)
    return total_died_str

def get_percent_change_total(df: pd.DataFrame) -> float:
    df_kpi_grouped = (df.groupby(by=["MONTH_YEAR"]).agg(report_count=("VAERS_ID", "count"))).reset_index()
    # sort by MONTH_YEAR
    if not df_kpi_grouped.empty:
        first_month = df_kpi_grouped.at[0,'report_count']
        last_month = df_kpi_grouped.at[(len(df_kpi_grouped)-1), 'report_count']
        if first_month == 0:
            pct_change = 'NaN'
        else:
            pct_change = ((last_month - first_month) / abs(first_month))*100
            pct_change = round(pct_change, 2)
    else:
        pct_change = "NaN"
    return pct_change

def get_percent_change_hosp(df: pd.DataFrame) -> float:
    df_hosp = df[df['HOSPITAL'] == 'Y']
    df_kpi_hosp = (df_hosp.groupby(by=["MONTH_YEAR"]).agg(report_count=("VAERS_ID", "count"))).reset_index()
    # sort by MONTH_YEAR
    if not df_kpi_hosp.empty:
        first_month = df_kpi_hosp.at[0,'report_count']
        last_month = df_kpi_hosp.at[(len(df_kpi_hosp)-1), 'report_count']
        if first_month == 0:
            pct_change = 'NaN'
        else:
            pct_change = ((last_month - first_month) / abs(first_month))*100
            pct_change = round(pct_change, 2)
    else:
        pct_change = "NaN"
    return pct_change

def get_percent_change_died(df: pd.DataFrame) -> float:
    df_died = df[df['DIED'] == 'Y']
    df_kpi_died = (df_died.groupby(by=["MONTH_YEAR"]).agg(report_count=("VAERS_ID", "count"))).reset_index()
    # sort by MONTH_YEAR
    if not df_kpi_died.empty:
        first_month = df_kpi_died.at[0,'report_count'] #this guy
        last_month = df_kpi_died.at[(len(df_kpi_died)-1), 'report_count']
        if first_month == 0:
            pct_change = 'NaN'
        else:
            pct_change = ((last_month - first_month) / abs(first_month))*100
            pct_change = round(pct_change, 2)
    else:
        pct_change = "NaN"
    return pct_change

