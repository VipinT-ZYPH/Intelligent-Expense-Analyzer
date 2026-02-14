import streamlit as st
import requests
from config import BACKEND_BASE_URL

st.title("Register")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    r = requests.post(
        f"{BACKEND_BASE_URL}/auth/register",
        json={"email": email, "password": password}
    )

    if r.status_code == 200:
        st.success("Registered successfully. Please login.")
    else:
        st.error("Registration failed")
