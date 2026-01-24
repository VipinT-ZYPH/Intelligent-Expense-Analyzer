import pandas as pd
import json
import os
from datetime import datetime


def build_or_update_profile(df, email, history_df):
    history_df["month"] = history_df["date"].dt.to_period("M")

    monthly_totals = history_df.groupby("month")["abs_amount"].sum()

    profile = {
        "email": email,
        "profile_updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "months_of_data": int(monthly_totals.shape[0]),
        "monthly_total": {
            "mean": round(monthly_totals.mean(), 2),
            "std": round(monthly_totals.std(), 2)
        },
        "category_stats": {}
    }

    cat_monthly = (
        history_df.groupby(["month", "category"])["abs_amount"]
        .sum()
        .reset_index()
    )

    for cat in cat_monthly["category"].unique():
        values = cat_monthly[cat_monthly["category"] == cat]["abs_amount"]
        profile["category_stats"][cat] = {
            "mean": round(values.mean(), 2),
            "std": round(values.std(), 2)
        }

    return profile


def save_profile(profile, base_path="data/profiles"):
    os.makedirs(base_path, exist_ok=True)
    path = os.path.join(base_path, f"{profile['email']}.json")
    with open(path, "w") as f:
        json.dump(profile, f, indent=4)
    return path
