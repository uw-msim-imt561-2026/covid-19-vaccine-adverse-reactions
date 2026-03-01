## Import Libraries
import pandas as pd
import streamlit as st

## Required cache decorator - needed for streamlit to function
@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
    df = pd.read_csv('data/west_states_filtered.csv')
    df["RECVDATE"] = pd.to_datetime(df["RECVDATE"])
    return df