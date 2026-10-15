import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

st.set_page_config(
    page_title="GroundWaterAI",
    page_icon="💧",
    layout="wide",
)

MODEL_PATH = "models/groundwater_model.joblib"
DATA_PATH = "data/demo_groundwater.csv"

bundle = joblib.load(MODEL_PATH)
model = bundle["model"]
FEATURES = bundle["features"]
metrics = bundle["metrics"]

df = pd.read_csv(DATA_PATH, parse_dates=["date"])

st.markdown(
    """
    <style>
    .main {background: #06100b;}
    .block-container {padding-top: 1.2rem;}
    .title {font-size: 42px; font-weight: 800; color: #8dff55;}
    .subtitle {font-size: 18px; color: #b7c5ba;}
    .risk {padding: 12px 18px; border-radius: 12px; font-size: 22px; font-weight: 700;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">💧 GroundWaterAI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-powered seasonal groundwater level prediction & early warning system</div>',
    unsafe_allow_html=True,
)

st.warning(
    "DEMO MODE: The bundled dataset is synthetically generated for the Infothon prototype. "
    "Replace it with verified CGWB/NWIC + rainfall data before claiming real-world accuracy."
)

st.sidebar.header("Prediction Inputs")

district = st.sidebar.selectbox("Location", sorted(df["district"].unique()))

latest = df[df["district"] == district].sort_values("date").iloc[-1]
recent = df[df["district"] == district].sort_values("date").tail(3)

rainfall = st.sidebar.slider(
    "Expected monthly rainfall (mm)",
    0.0, 300.0, float(latest["rainfall_mm"]), 1.0
)
rainfall_3m = st.sidebar.slider(
    "Expected 3-month rainfall (mm)",
    0.0, 700.0, float(recent["rainfall_mm"].sum()), 1.0
)
temperature = st.sidebar.slider(
    "Average temperature (°C)",
    15.0, 40.0, float(latest["temperature_c"]), 0.1
)
extraction = st.sidebar.slider(
    "Estimated extraction index",
    20.0, 120.0, float(latest["estimated_extraction_index"]), 1.0
)

next_month = 1 if latest["month"] == 12 else int(latest["month"] + 1)

input_row = pd.DataFrame([{
    "rainfall_mm": rainfall,
    "rainfall_3m_mm": rainfall_3m,
    "temperature_c": temperature,
    "estimated_extraction_index": extraction,
    "prev_groundwater_depth_m": float(latest["groundwater_depth_m"]),
    "month": next_month,
}])[FEATURES]

prediction = float(model.predict(input_row)[0])
current = float(latest["groundwater_depth_m"])
change = prediction - current

# Prototype risk thresholds; these are not universal scientific limits.
if prediction < 5:
    risk, risk_class = "LOW", "low"
elif prediction < 10:
    risk, risk_class = "MODERATE", "moderate"
elif prediction < 15:
    risk, risk_class = "HIGH", "high"
else:
    risk, risk_class = "CRITICAL", "critical"

if risk == "LOW":
    recommendation = "Maintain sustainable extraction and continue routine monitoring."
elif risk == "MODERATE":
    recommendation = "Monitor usage closely and increase local recharge measures."
elif risk == "HIGH":
    recommendation = "Reduce non-essential extraction and prioritize recharge interventions."
else:
    recommendation = "Immediate groundwater-use review and intensive recharge planning recommended."

c1, c2, c3, c4 = st.columns(4)
c1.metric("Current depth", f"{current:.2f} m")
c2.metric("Predicted depth", f"{prediction:.2f} m", f"{change:+.2f} m")
c3.metric("Rainfall input", f"{rainfall:.0f} mm")
c4.metric("Risk level", risk)

st.divider()

left, right = st.columns([1.55, 1])

with left:
    st.subheader(f"Groundwater Trend — {district}")
    chart_df = df[df["district"] == district].tail(48).copy()
    fig = px.line(
        chart_df,
        x="date",
        y="groundwater_depth_m",
        markers=True,
        labels={
            "date": "Date",
            "groundwater_depth_m": "Depth below ground (m)",
        },
        title="Historical groundwater depth",
    )
    fig.update_layout(height=380)
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Risk Assessment")
    st.markdown(
        f'<div class="risk">🟢 / 🟡 / 🟠 / 🔴 &nbsp; {risk}</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    st.write("**Recommendation**")
    st.info(recommendation)

    st.write("**Model inputs**")
    st.write({
        "Rainfall": f"{rainfall:.1f} mm",
        "3-month rainfall": f"{rainfall_3m:.1f} mm",
        "Temperature": f"{temperature:.1f} °C",
        "Extraction index": f"{extraction:.1f}",
    })

st.divider()

st.subheader("District Risk Snapshot")

snapshot = []
for d in sorted(df["district"].unique()):
    latest_d = df[df["district"] == d].sort_values("date").iloc[-1]
    prev_d = df[df["district"] == d].sort_values("date").iloc[-2]
    rain3_d = df[df["district"] == d].sort_values("date").tail(3)["rainfall_mm"].sum()
    row = pd.DataFrame([{
        "rainfall_mm": latest_d["rainfall_mm"],
        "rainfall_3m_mm": rain3_d,
        "temperature_c": latest_d["temperature_c"],
        "estimated_extraction_index": latest_d["estimated_extraction_index"],
        "prev_groundwater_depth_m": latest_d["groundwater_depth_m"],
        "month": 1 if latest_d["month"] == 12 else int(latest_d["month"] + 1),
    }])[FEATURES]
    p = float(model.predict(row)[0])
    if p < 5: r = "LOW"
    elif p < 10: r = "MODERATE"
    elif p < 15: r = "HIGH"
    else: r = "CRITICAL"
    snapshot.append({
        "District": d,
        "Current depth (m)": round(float(latest_d["groundwater_depth_m"]), 2),
        "Predicted depth (m)": round(p, 2),
        "Risk": r,
    })

snap = pd.DataFrame(snapshot)
st.dataframe(snap, use_container_width=True, hide_index=True)

with st.expander("Model information"):
    st.write("Algorithm: Gradient Boosting Regressor")
    st.write(f"Demo MAE: {metrics['MAE_m']:.3f} m")
    st.write(f"Demo RMSE: {metrics['RMSE_m']:.3f} m")
    st.write(f"Demo R²: {metrics['R2']:.3f}")
    st.caption(
        "These metrics are calculated on the synthetic demo dataset and must not be "
        "presented as field-validation results."
    )
