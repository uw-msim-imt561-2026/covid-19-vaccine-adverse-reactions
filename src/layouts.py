import pandas as pd
import streamlit as st

def header_metrics() -> None:
    #def header_metrics(df: pd.DataFrame) <--- update this when dataframe is ready
    """Rendering header metrics. Placeholder values are intentional."""
    c1, c2, c3 = st.columns(3)

    temporary_c4 = 0 # 0, increase; 1, decrease; 3, neither REPLACE THIS EVENTUALLY WITH ACTUAL LOGIC
    temporary_c5 = 1  # 0, increase; 1, decrease; 3, neither REPLACE THIS EVENTUALLY WITH ACTUAL LOGIC
    temporary_c6 = 2  # 0, increase; 1, decrease; 3, neither REPLACE THIS EVENTUALLY WITH ACTUAL LOGIC

    with c1:
        st.metric("Total adverse events  \nin current month",1)
        # This section just demonstrates how we can do preattentive attributes using markdowns.
        if temporary_c4 == 0:
            st.markdown(f''':green-background[:green[↑{100}%]]''')
        elif temporary_c4 == 1:
            st.markdown(f''':red-background[:red[↓{50}%]]''')
        elif temporary_c4 == 2:
            st.markdown(f''':yellow-background[:yellow[N/A]]''')
    with c2:
        st.metric("Total number of  \nHospitalizations",2)
        # This section just demonstrates how we can do preattentive attributes using markdowns.
        if temporary_c5 == 0:
            st.markdown(f''':green-background[:green[↑{100}%]]''')
        elif temporary_c5 == 1:
            st.markdown(f''':red-background[:red[↓{50}%]]''')
        elif temporary_c5 == 2:
            st.markdown(f''':yellow-background[:yellow[N/A]]''')
    with c3:
        st.metric("% of reported  \ndeaths",3)
        # This section just demonstrates how we can do preattentive attributes using markdowns.
        if temporary_c6 == 0:
            st.markdown(f''':green-background[↑INCREASE%]''')
        elif temporary_c6 == 1:
            st.markdown(f''':red-background[:red[↓{50}%]]''')
        elif temporary_c6 == 2:
            st.markdown(f''':yellow-background[:yellow[N/A]]''')

# Source: https://docs.streamlit.io/develop/api-reference/text/st.markdown


def body_layout_tabs() -> None:
    # body_layout_tabs(df: pd.DataFrame) <--- update this when dataframe is ready
    """Tabs layout with 3 default tabs."""
    t1, t2 = st.tabs(["Adverse Events", "Most Common Symptoms"])

    with t1:
        st.subheader("Welcome to Tab1")
        #plot_response_hist(df) #<-chart function here
        st.info("This is a chart!")

    with t2:
        st.subheader("Buenos dias, you're in Tab2")
        # plot_response_hist(df) #<-chart function here
        st.info("This is a chart again!")

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