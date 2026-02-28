import pandas as pd
import streamlit as st

def render_filters() -> dict:
   #def render_filters(df: pd.DataFrame) <-- make sure to put df: pd.DataFrame back when ready
    """Rendering filter widgets and returning the chosen values."""
    st.sidebar.header("Filters")

    vax_list = ['ALL'] + ['PFIZER',"MODERNA"] # was it just the two? did we want more?
    #vax_list = ["All"] + sorted(df["VAX_MANU"].unique().tolist()) <- replace when df functions

    state_list = ['ALL'] + ['CA',"OR","WA"]
    #state_list = ["All"] + sorted(df["STATE"].unique().tolist()) <- replace when df functions

    vax = st.sidebar.selectbox("Vaccine Type", vax_list, index=0)
    state = st.sidebar.multiselect("State", state_list, default=state_list)

    # Dosage Series slider
    min_rt, max_rt = float(0),float(7)
    #min_rt, max_rt = float(df["VAX_DOSE_SERIES"].min()), float(df["VAX_DOSE_SERIES"].max()) # df function ready?
    dosage = st.sidebar.slider(
        "Dosage Series",
        min_value=0.0,
        max_value=float(max_rt),
        value=(0.0, float(min(30.0, max_rt))),
        step=1.0,
    )

    #return {
        #"vax": vax,
        #"state": state,
        #"dosage": dosage,
    #}

def apply_filters():
    """Applying filter selections to the dataframe."""

    #def apply_filters(df: pd.DataFrame, selections: dict) -> pd.DataFrame:
    pass #remove this at some point

    #out = df.copy()

    #if selections["VAX_MANU"] != "All":
        #out = out[out["VAX_MANU"] == selections["VAX_MANU"]]

    #if selections["STATE"] == ["All"] or selections["STATE"] == []:
        #out = out
    #else:
       #out = out[out["STATE"].isin(selections["STATE"])]

    #lo, hi = selections["dosage"]
    #out = out[(out["VAX_DOSE_SERIES"] >= lo) & (out["VAX_DOSE_SERIES"] <= hi)]