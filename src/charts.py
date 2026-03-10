import pandas as pd
import streamlit as st # importing streamlit to get graphs to streamlit
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

'''This notebook stores all the functions for plotting the graphs you want on the dashboard'''

## Number of VAERS Reports Over Time - BARPLOT VERSION
def plot_reports_overtime_bar(df: pd.DataFrame):
    """Plotting a bar chart of the number of VAERS reports over time (per month)."""
    if type(df['ONSET_DATE']) == str:
        # sanity check to ensure datetime objects are present
        df['ONSET_DATE'] = df['ONSET_DATE'].astype('datetime64[ns]')
        # add Year, Month, and MonthYear columns
        df['ONSET_YEAR'] = df['ONSET_DATE'].dt.year
        df['ONSET_MONTHYEAR'] = df['ONSET_DATE'].dt.strftime('%Y-%m')

    if df.empty:
        st.info("No rows match your filters.")
        return

    # sort values + create groupby object
    reports_overtime = df.sort_values(by='ONSET_DATE')
    bar_grouped = reports_overtime.groupby(by=["ONSET_MONTHYEAR"]).agg(report_count=("VAERS_ID", 'count'))
    bar_grouped = bar_grouped.reset_index()

    # barplot (plotly.express version)
    labels = {'ONSET_MONTHYEAR':'Onset Month & Year', 'report_count':'Number of Reported Events'}
    fig = px.bar(bar_grouped, x="ONSET_MONTHYEAR", y="report_count", labels=labels, title='Number of COVID-19 VAERS Reports Over Time')

    # streamlit plot command
    st.plotly_chart(fig, width='stretch') # graph will be dynamically sized in layout

## Number VAERS Reports Over Time - LINEPLOT VERSION
def plot_reports_overtime_line(df: pd.DataFrame):
    """Plotting a line chart of the number of VAERS reports over time (per month)."""
    if type(df['ONSET_DATE']) == str:
        # sanity check to ensure datetime objects are present
        df['ONSET_DATE'] = df['ONSET_DATE'].astype('datetime64[ns]')
        # add Year, Month, and MonthYear columns
        df['ONSET_YEAR'] = df['ONSET_DATE'].dt.year
        df['ONSET_MONTHYEAR'] = df['ONSET_DATE'].dt.strftime('%Y-%m')

    if df.empty:
        st.info("No rows match your filters.")
        return

    # sort values + create groupby object
    reports_overtime = df.sort_values(by='ONSET_DATE')
    line_grouped = reports_overtime.groupby(by=["ONSET_MONTHYEAR"]).agg(report_count=("VAERS_ID", 'count'))
    line_grouped = line_grouped.reset_index()

    # line plot
    labels = {'ONSET_MONTHYEAR': 'Onset Month & Year', 'report_count': 'Number of Reported Events'}
    fig = px.line(line_grouped, x="ONSET_MONTHYEAR", y="report_count", labels=labels,
                  title='Number of COVID-19 VAERS Reports Over Time')

    # streamlit plot command
    st.plotly_chart(fig, width='stretch') # graph will be dynamically sized in layout

## Number VAERS Reports Over Time - LINEPLOT VERSION
def plot_reports_overtime_line_state(df: pd.DataFrame):
    """Plotting a line chart of the number of VAERS reports over time (per month)."""
    if type(df['ONSET_DATE']) == str:
        # sanity check to ensure datetime objects are present
        df['ONSET_DATE'] = df['ONSET_DATE'].astype('datetime64[ns]')
        # add Year, Month, and MonthYear columns
        df['ONSET_YEAR'] = df['ONSET_DATE'].dt.year
        df['ONSET_MONTHYEAR'] = df['ONSET_DATE'].dt.strftime('%Y-%m')

    if df.empty:
        st.info("No rows match your filters.")
        return

    # sort values + create groupby object
    reports_overtime = df.sort_values(by='ONSET_DATE')
    line_grouped = reports_overtime.groupby(by=["ONSET_MONTHYEAR","STATE"]).agg(report_count=("VAERS_ID", 'count'))
    line_grouped = line_grouped.reset_index()

    # line plot
    labels = {'ONSET_MONTHYEAR': 'Onset Month & Year', 'report_count': 'Number of Reported Events', 'STATE': 'State'}
    fig = px.line(line_grouped, x="ONSET_MONTHYEAR", y="report_count", labels=labels, color="STATE",
                  title='Number of COVID-19 VAERS Reports Over Time (State)')

    # streamlit plot command
    st.plotly_chart(fig, width='stretch') # graph will be dynamically sized in layout

def plot_reports_overtime_line_sex(df: pd.DataFrame):
    """Plotting a line chart of the number of VAERS reports over time (per month)."""
    if type(df['ONSET_DATE']) == str:
        # sanity check to ensure datetime objects are present
        df['ONSET_DATE'] = df['ONSET_DATE'].astype('datetime64[ns]')
        # add Year, Month, and MonthYear columns
        df['ONSET_YEAR'] = df['ONSET_DATE'].dt.year
        df['ONSET_MONTHYEAR'] = df['ONSET_DATE'].dt.strftime('%Y-%m')

    if df.empty:
        st.info("No rows match your filters.")
        return

    # sort values + create groupby object
    reports_overtime = df.sort_values(by='ONSET_DATE')
    line_grouped = reports_overtime.groupby(by=["ONSET_MONTHYEAR","SEX"]).agg(report_count=("VAERS_ID", 'count'))
    line_grouped = line_grouped.reset_index()

    # line plot
    labels = {'ONSET_MONTHYEAR': 'Onset Month & Year', 'report_count': 'Number of Reported Events', 'SEX': 'Sex'}
    fig = px.line(line_grouped, x="ONSET_MONTHYEAR", y="report_count", labels=labels, color="SEX",
                  title='Number of COVID-19 VAERS Reports Over Time (Sex)')

    # streamlit plot command
    st.plotly_chart(fig, width='stretch') # graph will be dynamically sized in layout

def plot_reports_overtime_line_vax(df: pd.DataFrame):
    """Plotting a line chart of the number of VAERS reports over time (per month)."""
    if type(df['ONSET_DATE']) == str:
        # sanity check to ensure datetime objects are present
        df['ONSET_DATE'] = df['ONSET_DATE'].astype('datetime64[ns]')
        # add Year, Month, and MonthYear columns
        df['ONSET_YEAR'] = df['ONSET_DATE'].dt.year
        df['ONSET_MONTHYEAR'] = df['ONSET_DATE'].dt.strftime('%Y-%m')

    if df.empty:
        st.info("No rows match your filters.")
        return

    # sort values + create groupby object
    reports_overtime = df.sort_values(by='ONSET_DATE')
    line_grouped = reports_overtime.groupby(by=["ONSET_MONTHYEAR","VAX_MANU"]).agg(report_count=("VAERS_ID", 'count'))
    line_grouped = line_grouped.reset_index()

    # line plot
    labels = {'ONSET_MONTHYEAR': 'Onset Month & Year', 'report_count': 'Number of Reported Events', 'VAX_MANU': 'Vaccine'}
    fig = px.line(line_grouped, x="ONSET_MONTHYEAR", y="report_count", labels=labels, color="VAX_MANU",
                  title='Number of COVID-19 VAERS Reports Over Time (Vaccine Type)')

    # streamlit plot command
    st.plotly_chart(fig, width='stretch') # graph will be dynamically sized in layout

## Most Common Symptoms
def plot_most_common_symptoms(df: pd.DataFrame):
    """Plotting a simple bar chart of the most common symptoms reported."""
    if df.empty:
        st.info("No rows match your filters.")
        return

    # plot counts of 10 most common symptoms
    symptom_counts = df['symptom'].value_counts()
    df_symptom_counts = symptom_counts.to_frame()
    df_symptom_counts = df_symptom_counts.reset_index()
    df_symptom_counts = df_symptom_counts.sort_values(by='count', ascending=False)
    df_symptom_counts[0:10]

    # plot bar chart
    labels = {'symptom': 'Symptom', 'count': 'Symptom Counts'}
    fig = px.bar(df_symptom_counts[0:10], x="count", y="symptom", labels=labels,
                 title='Most Commonly Reported COVID-19 VAERS Symptoms')

    # Source: https://plotly.com/python/builtin-colorscales/

    # streamlit plot command
    st.plotly_chart(fig, width='stretch') # graph will be dynamically sized in layout

## Patient Age Distribution
def plot_patient_ages(df: pd.DataFrame):
    if df.empty:
        st.info("No rows match your filters.")
        return

    labels = {'AGE_YRS': 'Patient Age (Years)', 'count': 'Number of VAERS Reports'}
    mean_age = round(df['AGE_YRS'].mean(), 2)
    median_age = round(df['AGE_YRS'].median(), 2)
    max_age = round(df['AGE_YRS'].max(), 2)
    min_age = round(df['AGE_YRS'].min(), 2)
    fig = px.histogram(df, x="AGE_YRS", title="Number of VAERS Reports by Patient Age", labels=labels)
    fig.add_vline(x=mean_age, line_width=3, annotation_text=("Average Age: " + str(mean_age)),
                  annotation_position="top left")
    fig.add_vline(x=median_age, line_width=3, annotation_text=("Median Age: " + str(median_age)),
                  annotation_position="top right")
    fig.add_vline(x=max_age, line_width=3, annotation_text=("Max Age: " + str(max_age)),
                  annotation_position="top right")
    fig.add_vline(x=min_age, line_width=3, annotation_text=("Min Age: " + str(min_age)),
                  annotation_position="top right")

    # streamlit plot command
    st.plotly_chart(fig, width='stretch') # graph will be dynamically sized in layout

## Number of Reports by Patient Sex
def plot_num_reports_sex(df: pd.DataFrame):
    if df.empty:
        st.info("No rows match your filters.")
        return

    # plotly bar chart
    labels = {'SEX': 'Patient Sex', 'report_count': 'Number of Adverse Events'}
    grouped_sex = df.groupby(by=['SEX']).agg(report_count=("VAERS_ID", 'count'))
    grouped_sex = grouped_sex.reset_index()
    fig = px.bar(grouped_sex, x="SEX", y="report_count", labels=labels, title='Number of VAERS Reports by Patient Sex', color="SEX")

    # streamlit plot command
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, width='stretch') # graph will be dynamically sized in layout

## Number of Reports by Patient Location
def plot_num_reports_loc(df: pd.DataFrame):
    if df.empty:
        st.info("No rows match your filters.")
        return

    # plotly bar chart
    labels = {'STATE': 'U.S. State or Territory', 'report_count': 'Number of Adverse Events'}
    grouped_state = df.groupby(by=['STATE']).agg(report_count=("VAERS_ID", 'count'))
    grouped_state = grouped_state.reset_index()
    grouped_state = grouped_state.sort_values(by='report_count', ascending=False)
    fig = px.bar(grouped_state, x="STATE", y="report_count", labels=labels, color="STATE",
                 title='Number of VAERS Reports by Patient Location')

    # streamlit plot command
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, width='stretch')  # graph will be dynamically sized in layout





