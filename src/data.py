## Import Libraries
import pandas as pd
import streamlit as st

## Required cache decorator - needed for streamlit to function
@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
    df = pd.read_csv('data/west_states_filtered.csv')
    df["RECVDATE"] = pd.to_datetime(df["RECVDATE"])
    df['SEX'] = df['SEX'].replace('F', 'Female')
    df['SEX'] = df['SEX'].replace('M', 'Male')
    df['SEX'] = df['SEX'].replace('U', 'Unknown or Undisclosed')
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

