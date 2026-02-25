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

# data.py (global)
- loads our cleaned data, what we reference
- tab view for each script below (3 total tabs, shows each others work)

# kpi.py (individual)
- somebody A, fixed atop always

# ot.py (individual)
- somebody A, 1 viz (maybe change to line viz cuz over time)
- suggested to take that over time viz from prototype and make separate tab for timebeing.

# crs.py (individual)
- somebody B

# vaers.py (individual)
- somebody C, counts of VAERS

# filters.py
- dosage series - multiselect
- sex - singleselect???
- location - multiselect
- prolly need - slider for time, see lab06 for how to do.

Plan:
1) Figure out how to load data in data.py
2) Somebody sets up other teammembers .py to load datasets from data.py
3) Somebody then takes this set up .py's into three tabs. Now people can just open app.py to see own work.
4) Everybody works in own .py, see above
5) People call out when they need to mess with app.py or filters.py to do that work. No sharing the individ. .py's