import pandas as pd
import streamlit as st

def render_filters(df: pd.DataFrame) -> dict:
    """Rendering filter widgets and returning the chosen values."""
    st.sidebar.header("FILTERS")
    st.sidebar.subheader("Vaccine",divider="grey")
    # Vaccine Type
    vax_list = ["All"] + sorted(df["VAX_MANU"].unique().tolist())
    vax = st.sidebar.selectbox("Vaccine Type", vax_list, index=0)

    # Dosage Series slider
    # min_rt, max_rt = float(0), float(7)  # get rid of this when df is ready
    min_rt, max_rt = float(df["VAX_DOSE_SERIES"].min()), float(df["VAX_DOSE_SERIES"].max())
    dosage = st.sidebar.slider(
        "Dosage Series",
        min_value=0.0,
        max_value=float(max_rt),
        value=(0.0, float(min(30.0, max_rt))),
        step=1.0,
    )
    st.sidebar.subheader("Demographic", divider="grey")
    sex_list = ["All"] + sorted(df["SEX"].unique().tolist())
    sex = st.sidebar.selectbox("Sex", vax_list, index=0)

    # State Location
    state_list = ["All"] + sorted(df["STATE"].unique().tolist())
    state = st.sidebar.multiselect("State", state_list, default=state_list)

    st.sidebar.subheader("", divider="grey")
    # Report Date slider
    #min_dt, max_dt = 0, 24  # get rid of this when df is ready
    min_dt, max_dt = df["RECVDATE"].min().to_pydatetime(), df["RECVDATE"].max().to_pydatetime()
    report_date = st.sidebar.slider(
        "Date of Report",
        min_value=min_dt,
        max_value=max_dt,
        value=(min_dt, max_dt),
        format="MM-DD-YY",
    )

    # Source: https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pydatetime.html
    ## ^ Makes it so the min and max of a datetime is returned in a way that Streamlit likes.

    st.sidebar.subheader("", divider="grey")
    st.sidebar.caption("IMT 561: Data Visualization  \nAJ Amrous, Em Stelter, S Brian Zavala")

    return {
        "vax": vax,
        "state": state,
        "dosage": dosage,
        "report_date": report_date
    }



def apply_filters(df: pd.DataFrame, selections: dict) -> pd.DataFrame:
    """Applying filter selections to the dataframe."""

    out = df.copy()

    if selections["vax"] != "All":
        out = out[out["VAX_MANU"] == selections["vax"]]

    if selections["state"] == ["All"] or selections["state"] == []:
        out = out
    else:
        out = out[out["STATE"].isin(selections["state"])]

    lo, hi = selections["dosage"]
    out = out[(out["VAX_DOSE_SERIES"] >= lo) & (out["VAX_DOSE_SERIES"] <= hi)]

    lo, hi = selections["report_date"]
    out = out[(out["RECVDATE"] >= lo) & (out["RECVDATE"] <= hi)]

    return out.reset_index(drop=True)