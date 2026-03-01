import pandas as pd
import streamlit as st
from src.charts import (plot_reports_overtime_bar,
                        plot_reports_overtime_line,
                        plot_patient_ages,
                        plot_num_reports_loc,
                        plot_num_reports_sex,
                        plot_most_common_symptoms)

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
            st.markdown(f''':red-background[:red[↑{100}%]]''')
        elif temporary_c4 == 1:
            st.markdown(f''':green-background[:green[↓{50}%]]''')
        elif temporary_c4 == 2:
            st.markdown(f''':yellow-background[:yellow[N/A]]''')
    with c2:
        st.metric("Total number of  \nHospitalizations",2)
        # This section just demonstrates how we can do preattentive attributes using markdowns.
        if temporary_c5 == 0:
            st.markdown(f''':red-background[:red[↑{100}%]]''')
        elif temporary_c5 == 1:
            st.markdown(f''':green-background[:green[↓{50}%]]''')
        elif temporary_c5 == 2:
            st.markdown(f''':yellow-background[:yellow[N/A]]''')
    with c3:
        st.metric("% of reported  \ndeaths",3)
        # This section just demonstrates how we can do preattentive attributes using markdowns.
        if temporary_c6 == 0:
            st.markdown(f''':red-background[:red[↑{100}%]]''')
        elif temporary_c6 == 1:
            st.markdown(f''':green-background[:green[↓{50}%]]''')
        elif temporary_c6 == 2:
            st.markdown(f''':yellow-background[:yellow[N/A]]''')

# Source: https://docs.streamlit.io/develop/api-reference/text/st.markdown


def body_layout_tabs(df) -> None:
    # body_layout_tabs(df: pd.DataFrame) <--- update this when dataframe is ready
    """Tabs layout with 3 default tabs."""
    t1, t2, t3 = st.tabs(["Events Over Time","Adverse Events", "Most Common Symptoms"])
    with t1:
        st.subheader("Events Over Time")
        tab_choice = st.radio(''':grey[Study the frequency of adverse reaction events reported over time.]''',
        ["Bar", "Line"],
        horizontal=True,
        )
        if tab_choice == "Bar":
            plot_reports_overtime_bar(df) #<-chart function here
            st.info("Bar graph.")
        elif tab_choice == "Line":
            # plot_reports_overtime_line(df) #<-chart function here
            st.info("Line chart.")

    with t2:
        st.subheader("Adverse Events")
        st.caption("Look into the frequency of adverse events across specific demographics.")
        # plot_patient_ages(df) #<-chart function here
        st.info("Age chart.")
        # plot_num_reports_sex(df) #<-chart function here
        st.info("Sex chart.")
        #  plot_num_reports_loc(df) #<-chart function here
        st.info("Location chart.")
    with t3:
        st.subheader("Most Common Symptoms")
        st.caption("Keep track of the most common symptoms reported with an adverse event.")
        # plot_most_common_symptoms(df) #<-chart function here
        st.info("MCS Chart.")
        st.info("Note: As per CDC Guideline, COVID‑19 illness may appear in VAERS reports when "
                "it occurs after vaccination; this reflects the system’s design to collect all "
                "post‑vaccination events for signal detection.")

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