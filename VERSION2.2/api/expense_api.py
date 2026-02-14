import requests
import streamlit as st
from config import BACKEND_BASE_URL

def get_expenses():
    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    r = requests.get(
        f"{BACKEND_BASE_URL}/expense",
        headers=headers
    )

    return r.json() if r.status_code == 200 else []

def add_expense(data: dict):
    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    r = requests.post(
        f"{BACKEND_BASE_URL}/expense",
        json=data,
        headers=headers
    )

    return r.status_code == 200
