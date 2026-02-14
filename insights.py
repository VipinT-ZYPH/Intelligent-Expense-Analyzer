import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from state.session import require_auth
from api.analysis_api import get_summary

require_auth()

st.title("Insights")

data = get_summary()

if not data or "category_breakdown" not in data:
    st.info("No data available yet")
else:
    df = pd.DataFrame(data["category_breakdown"])

    st.subheader("Category Breakdown")
    st.dataframe(df, use_container_width=True)

    fig, ax = plt.subplots()
    ax.bar(df["category"], df["total"])
    ax.set_xlabel("Category")
    ax.set_ylabel("Total Amount")

    st.pyplot(fig)
