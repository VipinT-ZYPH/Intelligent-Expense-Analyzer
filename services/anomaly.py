import json
import os


def load_profile(email, base_path="data/profiles"):
    path = os.path.join(base_path, f"{email}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)


def detect_anomalies(df, profile):
    results = {
        "total": None,
        "categories": []
    }

    total_spend = df["abs_amount"].sum()
    mean = profile["monthly_total"]["mean"]

    if mean > 0:
        pct = ((total_spend - mean) / mean) * 100
        if pct > 25:
            results["total"] = {
                "pct": round(pct, 1),
                "severity": "High" if pct > 50 else "Medium"
            }

    for cat, stats in profile["category_stats"].items():
        current = df[df["category"] == cat]["abs_amount"].sum()
        if stats["mean"] == 0:
            continue

        pct = ((current - stats["mean"]) / stats["mean"]) * 100
        if pct > 25:
            results["categories"].append({
                "category": cat,
                "pct": round(pct, 1),
                "severity": "High" if pct > 50 else "Medium"
            })

    return results
