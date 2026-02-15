import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from state.session import require_auth
from api.analysis_api import get_summary

require_auth()

st.title("Insights")

data = get_summary()

if not data or not data.get("by_category"):
    st.info("No data available yet")
else:
    breakdown = data["by_category"]

    df = pd.DataFrame({
        "category": breakdown.keys(),
        "total": breakdown.values()
    })

    st.subheader("Category Breakdown")
    st.dataframe(df, width="stretch")

    fig, ax = plt.subplots()
    ax.bar(df["category"], df["total"])
    ax.set_xlabel("Category")
    ax.set_ylabel("Total Amount")

    st.pyplot(fig)
