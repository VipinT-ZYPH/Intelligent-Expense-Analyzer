import streamlit as st
import pandas as pd
from state.session import require_auth, logout
from api.expense_api import get_expenses

require_auth()

st.title("Dashboard")

data = get_expenses()

if data:
    df = pd.DataFrame(data)
    total = df["amount"].sum()
    count = len(df)

    col1, col2 = st.columns(2)
    col1.metric("Total Expenses", f"₹ {total}")
    col2.metric("Number of Transactions", count)
else:
    st.info("No expense data available.")

if st.button("Logout"):
    logout()
