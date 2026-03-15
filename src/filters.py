import pandas as pd
import streamlit as st

def render_filters(df: pd.DataFrame) -> dict:
    """Rendering filter widgets and returning the chosen values."""
    st.sidebar.header("FILTERS")

    # REPORT DATE SECTION
    st.sidebar.subheader("Dates")
    # Report Date slider
    #min_dt, max_dt = 0, 24  # get rid of this when df is ready
    min_dt, max_dt = df["ONSET_DATE"].min().to_pydatetime(), df["ONSET_DATE"].max().to_pydatetime()
    report_date = st.sidebar.slider(
        "Date of Symptom Onset",
        min_value=min_dt,
        max_value=max_dt,
        value=(min_dt, max_dt),
        format="MM-DD-YY",
    )

    ## VACCINE SECTION
    st.sidebar.subheader("Vaccine Info")

    # Vaccine Type
    vax_list = ["All"] + sorted(df["VAX_MANU"].unique().tolist())
    vax = st.sidebar.selectbox("Manufacturer", vax_list, index=0)

    # Dosage Series slider
    # min_rt, max_rt = float(0), float(7)  # get rid of this when df is ready
    min_rt, max_rt = float(df["VAX_DOSE_SERIES"].min()), float(df["VAX_DOSE_SERIES"].max())
    dosage = st.sidebar.slider(
        "Dosage Series",
        min_value=1.0,
        max_value=float(max_rt),
        value=(1.0, float(min(30.0, max_rt))),
        step=1.0,
    )

    ## DEMOGRAPHICS SECTION
    st.sidebar.subheader("Patient Demographics")

    # Sex
    sex_list = ["All"] + sorted(df["SEX"].unique().tolist())
    sex = st.sidebar.selectbox("Sex", sex_list, index=0)

    # Age
    min_at, max_at = float(df["AGE_YRS"].min()), float(df["AGE_YRS"].max())
    age = st.sidebar.slider(
        "Age",
        min_value=float(min_at),
        max_value=float(max_at),
        value=(float(min_at), float(min(110.0, max_at))),
        step=1.0,
    )

    # State Location
    state_list = sorted(df["STATE"].unique().tolist())
    state = st.sidebar.multiselect("State", state_list, default=state_list)

    # Source: https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pydatetime.html
    ## ^ Makes it so the min and max of a datetime is returned in a way that Streamlit likes.

    #st.sidebar.subheader("", divider="grey")
    #st.sidebar.caption("IMT 561: Data Visualization  \nAJ Amrous, Em Stelter, S Brian Zavala")

    return {
        "vax": vax,
        "state": state,
        "dosage": dosage,
        "report_date": report_date,
        "sex": sex,
        "age": age
    }

def apply_filters(df: pd.DataFrame, selections: dict) -> pd.DataFrame:
    """Applying filter selections to the dataframe."""

    out = df.copy()
    # Vaccine Manufacturer
    if selections["vax"] != "All":
        out = out[out["VAX_MANU"] == selections["vax"]]

    # Sex
    if selections["sex"] != "All":
        out = out[out["SEX"] == selections["sex"]]

    # State Multiselect
    if not selections["state"]:
        out = out[out["STATE"] != out["STATE"]]
    else:
        out = out[out["STATE"].isin(selections["state"])]

    # All the sliders
    lo, hi = selections["dosage"]
    out = out[(out["VAX_DOSE_SERIES"] >= lo) & (out["VAX_DOSE_SERIES"] <= hi)]

    lo, hi = selections["age"]
    out = out[(out["AGE_YRS"] >= lo) & (out["AGE_YRS"] <= hi)]

    lo, hi = selections["report_date"]
    out = out[(out["ONSET_DATE"] >= lo) & (out["ONSET_DATE"] <= hi)]

    return out.reset_index(drop=True)