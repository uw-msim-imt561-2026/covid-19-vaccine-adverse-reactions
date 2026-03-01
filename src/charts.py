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

    # streamlit plot command
    st.plotly_chart(fig, width='stretch') # graph will be dynamically sized in layout

## Patient Age Distribution
def plot_patient_ages(df: pd.DataFrame):
    if df.empty:
        st.info("No rows match your filters.")
        return

    # plot distribution - patient age
    fig, ax = plt.subplots(figsize=(10, 8))
    patient_age_overall = sns.histplot(data=df, x="AGE_YRS", legend=True)

    mean_age = str(round(df['AGE_YRS'].mean(), 2))
    median_age = str(round(df['AGE_YRS'].median(), 2))
    max_age = str(round(df['AGE_YRS'].max(), 2))
    min_age = str(round(df['AGE_YRS'].min(), 2))

    plt.axvline(x=df.AGE_YRS.mean(),
                color='orange', lw=2.0, label='Average Age: ' + mean_age)
    plt.axvline(x=df.AGE_YRS.median(), color='blue', lw=2.0, label='Median Age: ' + median_age)
    plt.axvline(x=df.AGE_YRS.max(), color='red', lw=2.0, label='Max Age: ' + max_age)
    plt.axvline(x=df.AGE_YRS.min(), color='red', lw=2.0, label='Min Age: ' + min_age)
    plt.legend(loc='upper left')
    ax.set_xlabel('Patient Age in Years', fontsize=12)
    ax.set_ylabel('Number of VAERS Reports', fontsize=12)
    ax.set_title('Number of VAERS Reports by Patient Age', fontsize=16)
    plt.tight_layout()

    # streamlit plot command
    st.pyplot(fig, width='stretch') # graph will be dynamically sized in layout

## Number of Reports by Patient Sex
def plot_num_reports_sex(df: pd.DataFrame):
    if df.empty:
        st.info("No rows match your filters.")
        return

    #create groupby object
    bar_grouped = df.groupby(by=['SEX']).agg(report_count=("VAERS_ID", 'count'))

    # bar chart
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.barplot(data=bar_grouped, x='SEX', y='report_count', legend=False, width=0.5,
                gap=0.1)  # seaborn horizontal chart
    for container in ax.containers:
        ax.bar_label(container, fontsize=12)
    ax.set_xlabel('Number of Adverse Events', fontsize=12)
    ax.set_ylabel('Patient Sex', fontsize=12)
    ax.set_title('Number of VAERS Reports by Patient Sex', fontsize=14)
    plt.tight_layout()

    # streamlit plot command
    st.pyplot(fig, width='stretch') # graph will be dynamically sized in layout

## Number of Reports by Patient Location
# TODO - double-check filtering and create another view of this chart sorted by counts rather than alphabetical
def plot_num_reports_loc(df: pd.DataFrame):
    if df.empty:
        st.info("No rows match your filters.")
        return

    # create groupby object
    bar_grouped = df.groupby(["STATE"]).agg(report_count=("VAERS_ID", 'count'))
    # bar chart
    fig, ax = plt.subplots(figsize=(10, 20))
    sns.barplot(data=bar_grouped, x='report_count', y='STATE', legend=False, width=0.5, gap=0.1)  # seaborn horizontal chart
    for container in ax.containers:
        ax.bar_label(container, fontsize=12)
    ax.set_xlabel('Number of Adverse Events', fontsize=12)
    ax.set_ylabel('Patient Location (US State or Territory)', fontsize=12)
    ax.set_title('Number of COVID-19 VAERS Events by Patient Location', fontsize=14)
    plt.tight_layout()

    # streamlit plot command
    st.pyplot(fig, width='stretch') # graph will be dynamically sized in layout






