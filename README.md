# GroundWaterAI — Infothon MVP

AI-powered seasonal groundwater level prediction and early-warning prototype.

## What this MVP does

- Predicts groundwater depth from rainfall, temperature, previous groundwater level and an extraction index.
- Provides LOW / MODERATE / HIGH / CRITICAL risk classification.
- Gives a practical recommendation.
- Shows historical groundwater trends.
- Shows a district-level risk snapshot.
- Runs as a local Streamlit web app.

## Important data note

The bundled `data/demo_groundwater.csv` is **synthetically generated** so the project works immediately without waiting for external downloads.

**Do not present the demo model metrics as real-world accuracy.**

For the actual Infothon research version, replace the demo dataset with verified government data. The National Water Data Portal (NWDP/NWIC) provides Karnataka groundwater and rainfall datasets.

Useful official sources:

- NWDP Karnataka groundwater: https://www.nwdp.nwic.gov.in/en/dataset/ground-water-level-manual-daily-karnataka
- NWDP Karnataka rainfall: https://www.nwdp.nwic.gov.in/en/dataset/rainfall-manual-daily-karnataka
- CGWB groundwater monitoring: https://cgwb.gov.in/ground-water-level-monitoring
- IMD rainfall information: https://mausam.imd.gov.in/responsive/rainfallinformation.php

## Windows setup

Open Command Prompt inside this folder:

```text
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Or double-click:

```text
run_app.bat
```

The dashboard should open in your browser.

## Project structure

```text
GroundWaterAI_MVP/
│
├── app.py
├── run_app.bat
├── requirements.txt
│
├── data/
│   └── demo_groundwater.csv
│
├── models/
│   ├── groundwater_model.joblib
│   └── metrics.txt
│
├── scripts/
│   ├── train_model.py
│   └── download_real_data.py
│
└── docs/
    └── PPT_content.md
```

## ML model

Current demo model:

**Gradient Boosting Regressor**

Input features:

1. Monthly rainfall
2. 3-month rainfall
3. Temperature
4. Estimated extraction index
5. Previous groundwater depth
6. Month

Output:

**Predicted groundwater depth in metres below ground level.**

## Recommended Infothon development path

### Phase 1 — MVP
Use the bundled demo data and make the dashboard work.

### Phase 2 — Real data
Download Karnataka groundwater + rainfall data from NWDP/NWIC.

### Phase 3 — Data alignment
Aggregate rainfall by district/month and join it with groundwater observations.

### Phase 4 — Validation
Use a time-based split instead of a random split and report MAE, RMSE and R².

### Phase 5 — Deployment
Add district maps, alerts, model comparison and a recommendation engine.

## Judge demo flow

1. Open dashboard.
2. Select Mysuru.
3. Show current groundwater depth.
4. Change rainfall to a lower value.
5. Click/use the updated prediction.
6. Show predicted groundwater depth and risk.
7. Explain the recommendation.
8. Show the historical trend.
9. Show the district risk table.

## Strong one-line pitch

"We don't just measure groundwater depletion — we predict it before it becomes critical."
