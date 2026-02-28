import streamlit as st
import subprocess
import sys

## Grabs functions & scripts from other .py's
#from src import cleaning_VAERS
#from src import cleaning_vax
#from src import cleaning_symptoms
from src.data import merge_dfs
from src.layouts import header_metrics, body_layout_tabs

## Run cleaning scripts
# TODO - verify that the subprocess.run code below works for running cleaning scripts
#subprocess.run([f"{sys.executable}", "cleaning_VAERS.py"])
#subprocess.run([f"{sys.executable}", "cleaning_vax.py"])
#subprocess.run([f"{sys.executable}", "cleaning_symptoms.py"])
# Streamlit subprocess documentation: https://docs.streamlit.io/knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app

def main() -> None:
    st.set_page_config(
        page_title="COVID-19 VAERS Dashboard",
        layout="wide",
    )

    # -------------------------
    ## Header (sidebar by default)
    #st.title("COVID-19 VAERS Dashboard") <- replaced with st.image
    st.image("visualizations/logos/Header_VAERS.png",width='content',clamp=True) # prolly want to convert this to an .svg at some point
    st.caption("An interactive data visualization dashboard for adverse vaccine events and reactions.",text_alignment="center")
    # -------------------------

    ## Load Cached Data
    #df = merge_dfs()
    # sanity check
    #print(df.head(5))
    #st.write("Row count: ", len(df))
    #st.dataframe(df.head(5))

    # -------------------------
    ## Filters (sidebar by default)
    # render_filters returns a dictionary of user selections
    #selections = render_filters(df)

    # apply_filters returns a filtered dataframe based on selections
    #df_f = apply_filters(df, selections)
    # -------------------------

    # -------------------------
    ## KPIS
    header_metrics()

    st.divider()

    # -------------------------
    # Main body
    # -------------------------
    # Tabs layout by default (3 tabs)
    tab_choice = st.radio(
        "Choose a layout for the body (lab demo uses tabs; assignment can remix):",
        ["Tabs (3)", "Two Columns"],
        horizontal=True,
    )

    if tab_choice == "Tabs (3)":
        body_layout_tabs()
    else:
        # -------------------------
        # - left column: a chart
        # - right column: a table
        # -------------------------
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Response Time Distribution")
            #plot_response_hist(df_f)

        with col2:
            st.subheader("Filtered Rows")
            #st.dataframe(df_f, use_container_width=True, height=420)

if __name__ == "__main__":
        main()