import streamlit as st

## Grabs functions from other .py's
from src.layouts import header_metrics, body_layout_tabs

def main() -> None:
    st.set_page_config(
        page_title="COVID-19 VAERS Dashboard",
        layout="wide",
    )

    # -------------------------
    ## Header (sidebar by default)
    st.title("COVID-19 VAERS Dashboard")
    st.caption("TEAM VAERS: AJ Amrous, Em Stelter, and S Brian Zavala")
    # -------------------------


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
    #^ I believe this is redundant with a KPI TODO in filters.py.
    # The headers metrics already have functional placeholder metrics, with real calculations, once fixed in that TODO.

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