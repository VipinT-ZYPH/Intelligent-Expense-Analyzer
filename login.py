import streamlit as st
from api.auth_api import login_user

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    token = login_user(email, password)
    if token:
        st.session_state.token = token
        st.success("Login successful")
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Invalid credentials")
st.markdown("New user? Go to Register page from sidebar.")
