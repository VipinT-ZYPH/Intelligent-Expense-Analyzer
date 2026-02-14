import streamlit as st
import pandas as pd
from state.session import require_auth
from api.expense_api import get_expenses

require_auth()

st.title("Expenses")

data = get_expenses()

if not data:
    st.info("No expenses yet")
else:
    df = pd.DataFrame(data)
    df = df[["id", "category", "amount"]]
    st.dataframe(df, use_container_width=True)
