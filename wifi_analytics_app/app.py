import streamlit as st
import pandas as pd
import plotly.express as px
from insights import load_data, analyze_clusters

st.set_page_config(page_title="WiFi Analytics", layout="wide")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password123":
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials")

def main_dashboard():
    st.title("📊 WiFi Usage Dashboard")
    df = load_data()
    df_clustered = analyze_clusters(df)

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(df, x='location', color='device_type', title="Devices by Location")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.scatter(df_clustered, x='device_type_encoded', y='location_encoded', color='cluster',
                          title="Customer Segments")
        st.plotly_chart(fig2, use_container_width=True)

if st.session_state.logged_in:
    main_dashboard()
else:
    login()
