import streamlit as st
import pandas as pd
import plotly.express as px
import re
import os

from services.profile import build_or_update_profile, save_profile
from services.anomaly import load_profile, detect_anomalies


# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="Intelligent Expense Analyzer", layout="wide")
st.title("💸 Intelligent Expense Analyzer")


# ---------------------------
# Identity
# ---------------------------
email = st.text_input("Enter your email to load your profile")

if not email:
    st.info("Please enter your email to continue.")
    st.stop()

email_key = email.lower().replace("@", "_").replace(".", "_")

HISTORY_PATH = f"data/history/{email_key}.csv"


# ---------------------------
# Mode selector (THIS WAS MISSING)
# ---------------------------
mode = st.radio(
    "What do you want to do?",
    [
        "📊 View Historical Data",
        "📈 Monthly Analysis (Detect Anomalies)",
    ]
)


# ---------------------------
# Helpers
# ---------------------------
def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9 ]", "", str(text).lower())


def preprocess(df):
    df.columns = [c.lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = df["amount"].astype(float)
    df["abs_amount"] = df["amount"].abs()
    df["description_clean"] = df["description"].apply(clean_text)
    return df


CATEGORIES = {
    "Food": ["swiggy", "zomato", "pizza"],
    "Travel": ["uber", "ola", "train"],
    "Shopping": ["amazon", "flipkart"],
    "Bills": ["electricity", "recharge"],
    "Entertainment": ["netflix", "movie"]
}


def classify(text):
    for cat, kws in CATEGORIES.items():
        for kw in kws:
            if kw in text:
                return cat
    return "Other"


# =====================================================
# MODE 1 — VIEW HISTORICAL DATA ONLY
# =====================================================
if mode == "📊 View Historical Data":

    if not os.path.exists(HISTORY_PATH):
        st.warning("No historical data found for this user.")
        st.stop()

    history_df = pd.read_csv(HISTORY_PATH)
    history_df["date"] = pd.to_datetime(history_df["date"])

    st.subheader("📄 Stored Transactions")
    st.dataframe(history_df, use_container_width=True)

    st.subheader("📈 Spending Trend")
    monthly = (
        history_df.groupby(history_df["date"].dt.to_period("M"))["abs_amount"]
        .sum()
        .reset_index()
    )
    monthly["date"] = monthly["date"].astype(str)

    st.plotly_chart(
        px.line(monthly, x="date", y="abs_amount"),
        use_container_width=True
    )


# =====================================================
# MODE 2 — MONTHLY ANALYSIS (ONLY HERE)
# =====================================================
else:
    uploaded = st.file_uploader(
        "Upload CURRENT MONTH transactions CSV",
        type=["csv"]
    )

    if not uploaded:
        st.info("Upload a CSV to analyze this month.")
        st.stop()

    new_df = preprocess(pd.read_csv(uploaded))
    new_df["category"] = new_df["description_clean"].apply(classify)

    # Load history if exists
    if os.path.exists(HISTORY_PATH):
        history_df = pd.read_csv(HISTORY_PATH)
        history_df["date"] = pd.to_datetime(history_df["date"])
    else:
        history_df = None

    # ---------------------------
    # Anomaly detection (ONLY here)
    # ---------------------------
    profile = load_profile(email_key)

    if profile and profile["months_of_data"] > 1:
        anomalies = detect_anomalies(new_df, profile)

        st.subheader("🚨 Anomaly Report")

        if anomalies["total"]:
            st.warning(
                f"Total spend is {anomalies['total']['pct']}% higher "
                f"({anomalies['total']['severity']} severity)"
            )
        else:
            st.success("Total spending is within normal range.")

        for c in anomalies["categories"]:
            st.warning(
                f"{c['category']} spending ↑ {c['pct']}% "
                f"({c['severity']})"
            )
    else:
        st.info(
            "Not enough historical data yet. "
            "This month will be used to build your baseline."
        )

    # ---------------------------
    # AFTER analysis → update history
    # ---------------------------
    if history_df is not None:
        updated_history = pd.concat([history_df, new_df], ignore_index=True)
    else:
        updated_history = new_df.copy()

    os.makedirs("data/history", exist_ok=True)
    updated_history.to_csv(HISTORY_PATH, index=False)

    # Update profile
    profile = build_or_update_profile(new_df, email_key, updated_history)
    save_profile(profile)

    st.success("Monthly data analyzed and added to history.")

    st.subheader("📄 This Month's Transactions")
    st.dataframe(new_df, use_container_width=True)
