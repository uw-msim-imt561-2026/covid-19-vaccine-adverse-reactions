# covid-19-vaccine-adverse-reactions

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
streamlit run app.py
```

## Submission
- **Streamlit deployed link:** https://a9hkgrtvqdwsrpky48zxpk.streamlit.app/
- **GitHub repo link:** https://github.com/uw-msim-imt561-2026/covid-19-vaccine-adverse-reactions
- **Description:** (see below)

## PROJECT CONTEXT AND INTENDED USE

This is a student-led data visualization project developed for the UW Master of Information Management program. The primary project goal was for our team to practice building a streamlined dashboard for a specific stakeholder audience. This dashboard and any insights gleaned from it should not be taken as authoritative conclusions on the impacts of COVID-19 vaccines or their side-effects. (See “Ethical Concerns” for further detail.)

## DATASET DETAILS

Developed by the Food and Drug Administration (FDA) and the Centers for Disease Control and Prevention (CDC), the Vaccine Adverse Event Reporting System (VAERS) dataset is a collection of reported adverse medical reactions that patients have experienced after receiving a vaccine. Like all pharmaceutical drugs, vaccines can have negative side effects, some of which can be serious or deadly. The VAERS dataset focuses on those reactions, reported symptoms, clinical details, and limited patient demographic information. 

For this project, our team worked with a subset of the VAERS dataset, filtered for COVID-19 vaccinations between 2020 and 2024, assembled by Ayush Garg on Kaggle: COVID-19 World Vaccine Adverse Reactions. We have further filtered Garg’s dataset to focus our scope on the western United States and on COVID-19 vaccines developed by pharmaceutical developers Moderna and Pfizer.

**Team Interest:** Our team selected this dataset because we are interested in using data analytics and visualization to support public health initiatives and continued vaccine development. We felt that a robust dashboard tracking COVID-19 vaccine reactions would be a useful internal-facing tool for pharmaceutical developers like Pfizer and Moderna to reduce negative side effects, and a good opportunity for us to practice our dashboarding and visualization skills.

**Dataset Contents:** The VAERS COVID-19 dataset includes three CSV files: 

- **VAERSDATA**: Includes information about the patient, where the vaccination occurred, whether the patient experienced serious negative health outcomes, and other relevant clinical and demographic information. 
- **VAERSSYMPTOMS** *: Includes all adverse symptoms that the patient experienced as part of their reaction after vaccination. 
- **VAERSVAX** *: Includes details about the vaccine administered, e.g. manufacturer, lot number, dosage series, etc.

**Note: All datasets include a VAERS_ID variable that links records across files. VAERSVAX and VAERSDATA contain repeated VAERS_ID values because different rows capture different information for the same individual. In VAERSSYMPTOMS, only five symptoms can be recorded per row, so additional rows are created when a patient reports more than five symptoms, which also produces repeated VAERS_IDs. In VAERSVAX, duplicates occur when an individual has multiple vaccination records, such as receiving a two‑dose series like Moderna or Pfizer.*

## PROJECT STAKEHOLDERS
Our team’s imagined stakeholders are executives and heads of Research and Development for COVID-19 vaccine developers Pfizer and Moderna. These stakeholders fall into two categories:
1) **Medical experts** (a.k.a. "The Researchers" / “The R&D”): Individuals with strong medical and scientific backgrounds who work directly in research and development labs and evaluate vaccine safety signals. 
2) **Operations experts** (a.k.a "The Business-minded"): Individuals with business or operations backgrounds who make key decisions about manufacturing, resource allocation, and overall product strategy. These stakeholders need clear information about adverse effects in VAERS to interpret vaccine demand, anticipate operational needs, and understand the choices made by the Medical Experts, during their vaccine development.

Vaccine adverse reaction data matters to our stakeholders because they are obliged to monitor the negative side effects of their products and ensure they are not causing patients outsized harm (e.g. outcomes like hospitalization, death, or disablement). Ethically and financially, vaccine developers must work to improve future vaccine formulations to minimize negative side effects. In addition, our stakeholders face a political climate of vaccine hesitancy and mistrust. They may wish to use the insights from our dataset for marketing their products to external audiences (e.g., illustrating downward trends in adverse events as the COVID-19 vaccines have developed between 2020 and 2024).

Our stakeholders have asked us to analyze the VAERS dataset to accomplish the following specific goals:

1) Determine how the number of reported adverse COVID-19 vaccine reactions has changed over time. 
2) Confirm any trends in adverse events according to variables such as patient age, location (state), dosage series (i.e., shot 1 or 2), etc. 
3) Identify the most common symptoms associated with adverse COVID-19 vaccine reactions 
4) Present visual information that is interpretable by both medical experts and healthcare industry leaders with a range of technical knowledge when it comes to vaccine development.

## ETHICAL CONCERNS

**Vaccine Misinformation and Potential Misuse**

Due to the political climate surrounding vaccine hesitancy and mistrust, anti-vaccine groups have utilized VAERS data to spread disinformation regarding the risks of the COVID-19 to further broader conspiracy theories (Brumfiel, NPR, 2021), (Settles, Poynter, 2021). Care must be taken to use dashboard insights for purposes that are aligned with scientific consensus on vaccine efficacy and safety.

As stated above, this is a student project developed in the context of a ten-week data visualization course. We are not healthcare professionals, and we are not operating with pharmaceutical subject matter expertise. Due to time constraints, our user testing process involved convenience sampling. (We were ~not~ actually able to get the heads of Pfizer and Moderna R&D on Zoom.) We conducted mock interviews with more general users, whom we provided with a VAERS fact-sheet so they could role-play as our stakeholder audience. Any real-world application of the VAERS dataset should involve user testing with the intended stakeholder audience.

We have included a “Project Context and Intended Use” statement above to guard against potential misuse of this project.

**Dataset Scope & Data Accuracy**

The COVID-19 VAERS dataset was last updated in 2024 (Garg, Kaggle, 2026), representing VAERS reports submitted between 2020 and 2024, so more recent COVID-19 vaccine iterations are not represented in our analysis. A real-world context should include the COVID-19 VAERS data between 2024 and the present.

That said, any data sourced from the U.S. federal government should be considered with some skepticism. The current presidential administration has shown an eagerness to remove leadership from federal agencies publishing data that does not meet with executive approval. See: the firing of Erika McEntarfer from the Bureau of Labor Statistics in summer 2025 (Rugaber, Boston Globe, 2025). Given the anti-vaccine stance of the current head of the CDC (Merlan, Mother Jones, 2025), the current VAERS dataset should be approached with caution.

# REFERENCES
(see also “References” directory for PDF copies of the news articles cited below)

- Brumfiel, G. (June 14, 2021). *Anti-Vaccine Activists Use A Federal Database To Spread Fear About COVID Vaccines.* NPR.
https://www.npr.org/sections/health-shots/2021/06/14/1004757554/anti-vaccine-activists-use-a-federal-database-to-spread-fear-about-covid-vaccine.


- Garg, A. (2024). *COVID-19 World Vaccine Adverse Reactions.* Kaggle. Retrieved JAN 2026 from https://www.kaggle.com/datasets/ayushggarg/covid19-vaccine-adverse-reactions/data.


- Merlan, A. (November 22, 2025). *RFK Jr. Wants You to Know He’s Personally Responsible for Anti-Vax Misinformation on CDC Website.* Mother Jones. https://www.motherjones.com/politics/2025/11/robert-kennedy-jr-vaccine-misinformation-cdc-website/.


- Rugaber, C. (August 1, 2025). *Trump removes official overseeing jobs data after dismal employment report.* Boston Globe. https://www.bostonglobe.com/2025/08/01/business/trump-fires-bls-commissioner/.


- Settles, G. (October 5, 2021). *Claims that millions of people have died from the
COVID-19 vaccine are unfounded.* Poynter. https://www.poynter.org/fact-checking/2021/claims-that-millions-of-people-have-died-from-the-covid-19-vaccine-are-unfounded/.
