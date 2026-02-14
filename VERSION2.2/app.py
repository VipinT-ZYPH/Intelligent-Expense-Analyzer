import streamlit as st
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR))

st.set_page_config(page_title="Expense Analyzer", layout="wide")

st.title("Expense Analyzer")

if "token" in st.session_state:
    st.success("Logged in")
else:
    st.info("Please log in using the sidebar")
