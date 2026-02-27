# covid-19-vaccine-adverse-reactions

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
streamlit run app.py
```

## Submission
- **Streamlit deployed link:** asdf.
- **GitHub repo link:** asdf.
- **Description:** asdf.

# app.py (global)
- calls our .py
- layout - grab from Lab06

# cleaning_VAERS.py (global)
- cleans data for VAERS (references cleaning_VAERS.ipynb)

# cleaning_VAX.py (global)
- cleans data for VAX (references cleaning_VAX.ipynb)

# cleaning_symptoms.py (global)
- cleans data for symptoms (references cleaning_symptoms.ipynb)

# data.py (global)
- loads cleaned dataframes from the above scripts, what we reference
- merges cleaned dataframes from data_VAERS.py, data_VAX.py, data_symptoms.py into one dataframe
- filters cleaned dataframes for just rows where VAX_MANU = Pfizer or Moderna

# filters.py
- sets up filtering for the app
- dosage series - multiselect
- sex - singleselect???
- location - multiselect
- prolly need - slider for time, see lab06 for how to do.

# layouts.py
- sets up tab view for each charts.py script (see scripts below)
- 3 total tabs, each of us takes one tab - shows each other's work

# kpi.py (individual)
- somebody A, fixed atop always

# charts_overtime.py (individual)
- somebody A, 1 viz (maybe change to line viz cuz over time)
- suggested to take that over time viz from prototype and make separate tab for timebeing
- *We might change the barplot to a line plot

# charts_common_symptoms.py (individual)
- somebody B

# charts_vaers.py (individual)
- somebody C, counts of VAERS


Plan:
1) Figure out how to load data in data.py
2) Somebody sets up other teammembers .py to load datasets from data.py
3) Somebody then takes this set up .py's into three tabs. Now people can just open app.py to see own work.
4) Everybody works in own .py, see above
5) People call out when they need to mess with app.py or filters.py to do that work. No sharing the individ. .py's