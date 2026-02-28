import pandas as pd
import plotly.express as px
import streamlit as st # importing streamlit to get graphs to streamlit
import matplotlib.pyplot as plt
import seaborn as sns

'''This notebook stores all the functions for plotting the graphs you want on the dashboard'''


## Number of VAERS Reports Over Time
# TODO - change to lineplot? (test in visualizations.ipynb)
# TODO - Figure out if we need to include calls for Moderna & Pfizer plots or if this will be handled in filtering
def plot_reports_overtime_bar(df: pd.DataFrame):
    """Plotting a bar chart of the number of VAERS reports over time (per month)."""
    if type(df['ONSET_DATE']) == str:
        # sanity check to ensure datetime objects are present
        df['RECVDATE'] = df['RECVDATE'].astype('datetime64[ns]')
        df['DATEDIED'] = df['DATEDIED'].astype('datetime64[ns]')
        df['VAX_DATE'] = df['VAX_DATE'].astype('datetime64[ns]')
        df['ONSET_DATE'] = df['ONSET_DATE'].astype('datetime64[ns]')
        df['TODAYS_DATE'] = df['TODAYS_DATE'].astype('datetime64[ns]')
        df['RPT_DATE'] = df['RPT_DATE'].astype('datetime64[ns]')

        # add Year, Month, and MonthYear columns
        df['ONSET_YEAR'] = df['ONSET_DATE'].dt.year
        df['ONSET_MONTH'] = df['ONSET_DATE'].dt.strftime('%b')
        df['ONSET_MONTHYEAR'] = df['ONSET_DATE'].dt.strftime('%Y-%m')

    if df.empty:
        st.info("No rows match your filters.")
        return

    # sort values + create groupby object
    bar_reports_overtime = df.sort_values(by='ONSET_DATE')
    bar_grouped = bar_reports_overtime.groupby(by=["ONSET_MONTHYEAR"]).agg(report_count=("VAERS_ID", 'count'))

    # set up bar chart
    fig, ax = plt.subplots(figsize=(25, 15))
    frequency_reports_over_time_OVERALL = sns.barplot(data=bar_grouped, x="ONSET_MONTHYEAR", y="report_count",
                                                      width=0.5, gap=0.1)
    for container in ax.containers:
        ax.bar_label(container, fontsize=14)
    ax.set_xlabel('Onset Month + Year', fontsize=18)
    ax.tick_params("x", rotation=45)
    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.tick_params(axis='both', which='minor', labelsize=14)
    ax.set_ylabel('Number of Adverse Event Reports', fontsize=18)
    ax.set_title('Number of COVID-19 VAERS Reports Over Time', fontsize=20)
    plt.tight_layout()

    # streamlit plot command
    st.plotly_chart(fig, use_container_width=True) # graph will be dynamically sized in layout


## Most Common Symptoms
# TODO - maybe change title to 'Top 10 Reported Symptoms'
# TODO - figure out if we need to include functions for filtered graphs, or if filters.py will handle
def plot_most_common_symptoms(df: pd.DataFrame):
    """Plotting a simple bar chart of the most common symptoms reported."""
    if df.empty:
        st.info("No rows match your filters.")
        return

    # get counts of 10 most common symptoms
    symptom_counts = df['symptom'].value_counts()
    df_symptom_counts = symptom_counts.to_frame()

    # plot bar chart
    fig, ax = plt.subplots(figsize=(10, 8))
    most_common_symptoms_overall = sns.barplot(data=df_symptom_counts[0:10], x="count", y="symptom", hue='symptom',
                                               width=0.5, gap=0.1)
    for container in ax.containers:
        ax.bar_label(container, fontsize=10, label_type='center', color='black')
    ax.set_xlabel('Symptom Counts', fontsize=14)
    ax.set_ylabel('Symptom', fontsize=14)
    ax.set_title('Most Common COVID-19 VAERS Symptoms', fontsize=18)
    plt.tight_layout()

    # streamlit plot command
    st.plotly_chart(fig, use_container_width=True)

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
    st.plotly_chart(fig, use_container_width=True)

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
    st.plotly_chart(fig, use_container_width=True)

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
    st.plotly_chart(fig, use_container_width=True)






