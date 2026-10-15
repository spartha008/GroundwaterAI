# 💧 GroundWaterAI — Groundwater Prediction & Risk Assessment

An ML-powered prototype that predicts seasonal groundwater levels and classifies groundwater depletion risk using rainfall, temperature, historical groundwater depth, and estimated water extraction.

Built with Python and Streamlit as a hands-on machine learning and data science project.

## 🚀 Features

- **Groundwater Prediction:** Estimates groundwater depth using a Gradient Boosting Regressor.
- **Risk Classification:** Categorizes groundwater conditions into LOW, MODERATE, HIGH, and CRITICAL risk levels.
- **Interactive Dashboard:** Adjust input parameters and explore updated predictions.
- **Historical Trend Visualization:** Displays groundwater depth trends over time.
- **Risk Assessment:** Provides recommendations based on the predicted risk level.
- **District-Level Overview:** Presents a snapshot of groundwater risk across locations.

## 🛠️ Tech Stack

- **Language:** Python
- **Dashboard:** Streamlit
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly
- **Version Control:** Git and GitHub

## 🧠 Machine Learning Approach

The prototype uses a **Gradient Boosting Regressor** to estimate groundwater depth in metres below ground level.

### Input Features

1. Monthly rainfall
2. Three-month cumulative rainfall
3. Average temperature
4. Estimated groundwater extraction index
5. Previous groundwater depth
6. Month of the year

### Output

- Predicted groundwater depth
- Groundwater risk category
- Risk-based recommendations

## 📊 Data & Limitations

**Current status: Demonstration prototype.**

The bundled dataset (`data/demo_groundwater.csv`) contains synthetically generated data to make the application runnable without external data downloads.

The current predictions and model metrics are intended for demonstration purposes and **do not establish real-world forecasting accuracy**.

The next development step is to integrate verified groundwater and rainfall observations from official sources, align the datasets by location and time, and evaluate performance using time-based validation.

### Potential Data Sources

- [NWDP — Karnataka Groundwater Data](https://www.nwdp.nwic.gov.in/en/dataset/ground-water-level-manual-daily-karnataka)
- [NWDP — Karnataka Rainfall Data](https://www.nwdp.nwic.gov.in/en/dataset/rainfall-manual-daily-karnataka)
- [Central Ground Water Board (CGWB)](https://cgwb.gov.in/ground-water-level-monitoring)
- [India Meteorological Department (IMD)](https://mausam.imd.gov.in/responsive/rainfallinformation.php)

## 💻 Getting Started

### Prerequisites

- Python installed on your system
- Git (optional, for cloning the repository)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/sparthaa08/GroundWaterAI.git
cd GroundWaterAI
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the environment on Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can skip activation and use the environment's Python executable directly.

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the application**

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 📁 Project Structure

```text
GroundWaterAI/
├── app.py
├── run_app.bat
├── requirements.txt
├── data/
│   └── demo_groundwater.csv
├── models/
│   ├── groundwater_model.joblib
│   └── metrics.txt
├── scripts/
│   ├── train_model.py
│   └── download_real_data.py
└── docs/
    └── PPT_content.md
```

*Note: The structure above reflects the intended project layout. File availability may vary by repository version.*

## 🔭 Future Improvements

- Integrate verified government groundwater and rainfall datasets.
- Improve feature engineering and data preprocessing.
- Evaluate predictions using time-based train/test splits.
- Compare multiple regression algorithms.
- Add interactive district maps and location-based analysis.
- Develop more robust early-warning alerts and recommendations.
- Deploy the dashboard for public access.

## 🎯 What I Learned

- Building an interactive dashboard with Streamlit.
- Applying a regression model to a real-world environmental problem.
- Organizing a Python machine learning project