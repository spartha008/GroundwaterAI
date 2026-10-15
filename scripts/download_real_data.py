"""
Optional real-data downloader.

Sources are National Water Data Portal / NWIC.
Run this script only when you want to replace the demo data.

The URLs below were identified from the public NWDP resource pages.
After downloading, inspect column names and build a location/date-aligned
feature table before training the model.

Groundwater:
Karnataka Manual Monthly 2021-2025

Rainfall:
Karnataka Manual Daily 2021-2022
Karnataka Manual Daily 2023-2025
"""

from pathlib import Path
import requests

OUT = Path("data/raw")
OUT.mkdir(parents=True, exist_ok=True)

FILES = {
    "groundwater_2021_2025.csv":
        "https://nwdp.nwic.gov.in/dataset/1cbc78e5-42e2-4140-a584-ec752c994955/resource/ac075bf0-3894-4387-89c7-ae242f2cb060/download/karnataka_man_gw_wl_monthly_data_2021_2025.csv",
    "rainfall_2021_2022.csv":
        "https://nwdp.nwic.gov.in/dataset/fde650de-0c37-4864-972d-6bfcfd5fb200/resource/53fc54f7-43bf-4b46-bd88-2a421e4ffc61/download/karnataka_rainfall_data_2021_2022.csv",
    "rainfall_2023_2025.csv":
        "https://nwdp.nwic.gov.in/dataset/fde650de-0c37-4864-972d-6bfcfd5fb200/resource/656c5b3a-b6f5-44ee-adeb-710c015037a9/download/karnataka_rainfall_data_2023_2025.csv",
}

for name, url in FILES.items():
    path = OUT / name
    print(f"Downloading {name} ...")
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    path.write_bytes(r.content)
    print(f"Saved: {path} ({len(r.content)/1024/1024:.1f} MB)")

print("\nDownloads complete.")
print("Next: inspect the CSV columns and aggregate both datasets by district/month.")
