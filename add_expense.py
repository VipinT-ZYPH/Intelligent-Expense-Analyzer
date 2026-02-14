import streamlit as st
from state.session import require_auth
from api.expense_api import add_expense

require_auth()

st.title("Add Expense")

amount = st.number_input("Amount", min_value=0.0)
category = st.text_input("Category")

if st.button("Save"):
    if category.strip() == "":
        st.warning("Category required")
    else:
        success = add_expense({
            "amount": amount,
            "category": category
        })

        if success:
            st.success("Saved")
        else:
            st.error("Failed")
