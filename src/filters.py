import pandas as pd
import streamlit as st

def render_filters(df: pd.DataFrame) -> dict:
    """Rendering filter widgets and returning the chosen values."""
    st.sidebar.header("Filters")

    #vax_list = ['ALL'] + ['PFIZER',"MODERNA"] # get rid of this when df is ready
    vax_list = ["All"] + sorted(df["VAX_MANU"].unique().tolist())

    #state_list = ['ALL'] + ['CA',"OR","WA"] # get rid of this when df is ready
    state_list = ["All"] + sorted(df["STATE"].unique().tolist())

    vax = st.sidebar.selectbox("Vaccine Type", vax_list, index=0)
    state = st.sidebar.multiselect("State", state_list, default=state_list)

    # Dosage Series slider
    min_rt, max_rt = float(0), float(7)  # get rid of this when df is ready
    # min_rt, max_rt = float(df["VAX_DOSE_SERIES"].min()), float(df["VAX_DOSE_SERIES"].max()) # df function ready?
    dosage = st.sidebar.slider(
        "Dosage Series",
        min_value=0.0,
        max_value=float(max_rt),
        value=(0.0, float(min(30.0, max_rt))),
        step=1.0,
    )

    # Report Date slider
    min_dt, max_dt = 0, 24  # get rid of this when df is ready
    # min_dt, max_dt = df["RECVDATE"].min(), df["RECVDATE"].max()  # I am not sure this will work, educated guess ¯\_(ツ)_/¯
    report_date = st.sidebar.slider(
        "Date of Report",
        min_value=min_dt,
        max_value=max_dt,
        value=(min_dt, max_dt),
        # step=???
    )

    return {
        "vax": vax,
        "state": state,
        #"dosage": dosage,
        #"report_date": report_date
    }
    st.sidebar.divider()
    st.sidebar.caption("IMT 561: Data Visualization  \nAJ Amrous, Em Stelter, S Brian Zavala")

def apply_filters(df: pd.DataFrame, selections: dict) -> pd.DataFrame:
    """Applying filter selections to the dataframe."""

    out = df.copy()

    if selections["vax"] != "All":
        out = out[out["vax"] == selections["vax"]]

    if selections["state"] == ["All"] or selections["state"] == []:
        out = out
    else:
       out = out[out["state_list"].isin(selections["state"])]

    #lo, hi = selections["dosage"]
    #out = out[(out["VAX_DOSE_SERIES"] >= lo) & (out["VAX_DOSE_SERIES"] <= hi)]

    #lo, hi = selections["RECVDATE"]
    #out = out[(out["RECVDATE"] >= lo) & (out["RECVDATE"] <= hi)]