import streamlit as st

def require_auth():
    if "token" not in st.session_state:
        st.warning("Please log in first")
        st.switch_page("pages/login.py")

def logout():
    st.session_state.clear()
    st.switch_page("pages/login.py")
