import pandas as pd
import streamlit as st

def header_metrics() -> None:
    #def header_metrics(df: pd.DataFrame) <--- update this when dataframe is ready
    """Rendering header metrics. Placeholder values are intentional."""
    c1, c2, c3 = st.columns(3)
    c4, c5, c6 = st.columns(3)

    with c1:
        st.metric("KPI1",1)
    with c2:
        st.metric("KPI2",2)
    with c3:
        st.metric("KPI2",3)
    with c4:
        st.metric("pre1",1)
    with c5:
        st.metric("pre2",2)
    with c6:
        st.metric("pre3",3)



def body_layout_tabs() -> None:
    # body_layout_tabs(df: pd.DataFrame) <--- update this when dataframe is ready
    """Tabs layout with 3 default tabs."""
    t1, t2, t3 = st.tabs(["Tab1", "Tab2", "Tab3"])

    with t1:
        st.subheader("Welcome to Tab1")
        #plot_response_hist(df) #<-chart function here
        st.info("This is a chart!")

    with t2:
        st.subheader("Buenos dias, you're in Tab2")
        # plot_response_hist(df) #<-chart function here
        st.info("This is a chart again!")

    with t3:
        st.subheader("Guess what, you're in Tab3")
        # plot_response_hist(df) #<-chart function here
        st.info("This is a really cool chart!")

        # If we want people to download our data, we'd use this guy in some way.
        #st.download_button(
            #label="Download CSV",
            #data=df.to_csv(index=False),
            #file_name="sample.csv",
            #mime="text/csv",
            #icon=":material/download:",
        #)
        ## Source: https://docs.streamlit.io/develop/api-reference/widgets/st.download_button
        ## Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html