import pandas as pd
import streamlit as st
from src.charts import (plot_reports_overtime_bar,
                        plot_reports_overtime_line,
                        plot_reports_overtime_line_state,
                        plot_reports_overtime_line_sex,
                        plot_reports_overtime_line_vax,
                        plot_patient_ages,
                        plot_num_reports_loc,
                        plot_num_reports_sex,
                        plot_most_common_symptoms)
from src.data import (get_total_events_kpi,
                      get_total_hosp_kpi,
                      get_total_died_kpi,
                      get_percent_change_total,
                      get_percent_change_hosp,
                      get_percent_change_died,
                      get_prev_month,
                      get_last_month)

def header_metrics(df: pd.DataFrame) -> None:
    #def header_metrics(df: pd.DataFrame) <--- update this when dataframe is ready
    """Rendering header metrics. Placeholder values are intentional."""
    c1, c2, c3 = st.columns(3)

    # calculate KPIs
    total_events = get_total_events_kpi(df)
    total_hosp = get_total_hosp_kpi(df)
    total_died = get_total_died_kpi(df)
    pct_change_total = get_percent_change_total(df)
    pct_change_hosp = get_percent_change_hosp(df)
    pct_change_died = get_percent_change_died(df)

    # metric help messages
    m1_help = "Total number of adverse events reported in the selected onset‑date range. Percent change compares this total to the previous set period."
    m2_help = "Total hospitalizations linked to adverse events in the selected onset‑date range. Percent change shows how this count shifted from the prior set period."
    m3_help = "Total deaths associated with adverse events in the selected onset‑date range. Percent change reflects the difference from the previous set period."

    with c1:
        st.metric("Total adverse events  \nover time",total_events,help=m1_help)
        if isinstance(pct_change_total, str):
            st.markdown(f''':yellow-background[:yellow[NaN]]''')
        else:
            if pct_change_total >= 0:
                st.markdown(f''':red-background[:red[↑{pct_change_total}%]]''')
            else:
                pct_change_total = pct_change_total * -1
                st.markdown(f''':green-background[:green[↓{pct_change_total}%]]''')
    with c2:
        st.metric("Total hospitalizations  \nover time",total_hosp,help=m2_help)
        if isinstance(pct_change_hosp, str):
            st.markdown(f''':yellow-background[:yellow[NaN]]''')
        else:
            if pct_change_hosp >= 0:
                st.markdown(f''':red-background[:red[↑{pct_change_hosp}%]]''')
            else:
                pct_change_hosp = pct_change_hosp * -1
                st.markdown(f''':green-background[:green[↓{pct_change_hosp}%]]''')
    with c3:
        st.metric("Total deaths  \nover time",total_died,help=m3_help)
        if isinstance(pct_change_died, str):
            st.markdown(f''':yellow-background[:yellow[NaN]]''')
        else:
            if pct_change_died >= 0:
                st.markdown(f''':red-background[:red[↑{pct_change_died}%]]''')
            else:
                pct_change_died = pct_change_died * -1
                st.markdown(f''':green-background[:green[↓{pct_change_died}%]]''')

    st.markdown("The percent change for each of the above metrics is calculated between the **last month** and **immediate previous month** of the selected date range.")
    st.markdown("*Last Month*: " + str(get_last_month(df)))
    st.markdown("*Immediate Previous Month*: " + str(get_prev_month(df)))

# Source: https://docs.streamlit.io/develop/api-reference/text/st.markdown

def body_layout_tabs(df) -> None:
    # body_layout_tabs(df: pd.DataFrame) <--- update this when dataframe is ready
    """Tabs layout with 3 default tabs."""
    t1, t2, t3, t4 = st.tabs(["Events Over Time","Adverse Events Demographics", "Most Common Symptoms", "Table View"])
    with t1:
        st.subheader("Events Over Time")
        tab_choice = st.radio(''':grey[Study the number of adverse reaction events reported over time.]''',
        ["Overall", "State","Sex","Vaccine Type"],
        horizontal=True,
        )
        #if tab_choice == "Bar":
            #plot_reports_overtime_bar(df) #<-chart function here
        if tab_choice == "Overall":
            plot_reports_overtime_line(df) #<-chart function here
        elif tab_choice == "State":
            plot_reports_overtime_line_state(df)  # <-chart function here
        elif tab_choice == "Sex":
            plot_reports_overtime_line_sex(df)  # <-chart function here
        elif tab_choice == "Vaccine Type":
            plot_reports_overtime_line_vax(df)  # <-chart function here

    with t2:
        st.subheader("Adverse Events by Patient Demographics")
        st.caption("Study the number of adverse events reported across specific patient demographics.")
        plot_patient_ages(df) #<-chart function here
        plot_num_reports_sex(df) #<-chart function here
        plot_num_reports_loc(df) #<-chart function here

    with t3:
        st.subheader("Most Common Symptoms")
        st.caption("Keep track of the most common symptoms reported with an adverse event.")
        plot_most_common_symptoms(df) #<-chart function here
        st.info("Note: VAERS is a self reported system. This means that anyone can submit any health event that"
                " happens after vaccination, even when the event may not be caused by the vaccine. This includes"
                " COVID-19 illness, unrelated medical issues, or entries such as \"no adverse event.\"")

    with t4:
        # If we want people to download our data, we'd use this guy in some way.
        st.dataframe(data=df)
        st.download_button(
            label="Download CSV",
            data=df.to_csv(index=False),
            file_name="west_states_filtered_v2.csv",
            mime="text/csv",
            icon=":material/download:",
        )

        ## Source: https://docs.streamlit.io/develop/api-reference/widgets/st.download_button
        ## Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html