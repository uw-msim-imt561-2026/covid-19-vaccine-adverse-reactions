import streamlit as st

## Grabs functions & scripts from other .py's
from src.data import load_data
from src.layouts import header_metrics, body_layout_tabs
from src.filters import render_filters, apply_filters

def main() -> None:
    st.set_page_config(
        page_title="COVID-19 VAERS Dashboard",
        layout="wide",
    )

    # -------------------------
    ## Header (sidebar by default)
    #st.title("COVID-19 VAERS Dashboard") <- replaced with st.image
    st.image("visualizations/logos/Header_VAERS.png",width='content',clamp=True) # prolly want to convert this to an .svg at some point
    st.caption("An interactive data visualization dashboard for adverse vaccine events and reactions.",text_alignment="left")
    # -------------------------

    ## Load Cached Data
    df = load_data()

    # sanity check
    st.write("Row count: ", len(df))
    st.dataframe(df.head(5))

    # -------------------------
    ## Filters (sidebar by default)
    # render_filters returns a dictionary of user selections
    selections = render_filters()

    # apply_filters returns a filtered dataframe based on selections
    #df_f = apply_filters(df, selections)
    # -------------------------

    # -------------------------
    ## KPIS
    st.subheader("Key Insights",divider="grey")
    header_metrics()

    # -------------------------
    # Main body
    # -------------------------
    st.subheader("Visualizations", divider="grey")
    body_layout_tabs(df)

    # -------------------------
    # Alt. Main body from Lab06; look at table with a specific visual
    # -------------------------
    # Tabs layout by default (3 tabs)
    #tab_choice = st.radio(
        #"Choose a layout for the body (lab demo uses tabs; assignment can remix):",
        #["Tabs (3)", "Two Columns"],
        #horizontal=True,
    #)

    #if tab_choice == "Tabs (3)":
        #body_layout_tabs()
    #else:
        # -------------------------
        # - left column: a chart
        # - right column: a table
        # -------------------------
        #col1, col2 = st.columns(2)
        #with col1:
            #st.subheader("Response Time Distribution")
            #plot_response_hist(df_f)

        #with col2:
            #st.subheader("Filtered Rows")
            #st.dataframe(df_f, use_container_width=True, height=420)

if __name__ == "__main__":
        main()