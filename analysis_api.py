import requests
import streamlit as st
from config import BACKEND_BASE_URL

def get_summary():
    headers = {
        "Authorization": f"Bearer {st.session_state.token}"
    }

    r = requests.get(
        f"{BACKEND_BASE_URL}/analysis/summary",
        headers=headers
    )

    if r.status_code == 200:
        return r.json()
    return {}
