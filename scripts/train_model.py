import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

DATA_PATH = "data/demo_groundwater.csv"
MODEL_PATH = "models/groundwater_model.joblib"

features = [
    "rainfall_mm",
    "rainfall_3m_mm",
    "temperature_c",
    "estimated_extraction_index",
    "prev_groundwater_depth_m",
    "month",
]
target = "groundwater_depth_m"

df = pd.read_csv(DATA_PATH)
X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

model = GradientBoostingRegressor(
    n_estimators=250,
    learning_rate=0.035,
    max_depth=3,
    random_state=42,
    loss="huber",
)
model.fit(X_train, y_train)

pred = model.predict(X_test)
mae = mean_absolute_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

joblib.dump(
    {
        "model": model,
        "features": features,
        "metrics": {"MAE_m": mae, "RMSE_m": rmse, "R2": r2},
        "mode": "DEMO DATASET",
    },
    MODEL_PATH,
)

print(f"MAE  : {mae:.3f} m")
print(f"RMSE : {rmse:.3f} m")
print(f"R2   : {r2:.3f}")
print(f"Saved model to {MODEL_PATH}")
