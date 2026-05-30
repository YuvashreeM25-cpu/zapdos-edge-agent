import streamlit as st
import json
import os
import pandas as pd
import time

st.set_page_config(page_title="Zapdos Edge Monitor", layout="wide")
st.title("🏭 Zapdos Digital Factory - Edge Agent")

HISTORY_FILE = "../data/history.json"
DATA_FILE = "../data/live_stream.json"

# 1. Load Data
try:
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
except: data = None

# 2. Display Live Metrics
if data:
    st.subheader("📡 Live Sensor Data")
    col1, col2, col3 = st.columns(3)
    col1.metric("Vibration", f"{data['vibration']} Hz")
    col2.metric("Heat", f"{data['heat']} °C")
    col3.metric("Pressure", f"{data['pressure']} Bar")

# 3. Load History Table
st.subheader("📊 Anomaly History Log")
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        history_data = json.load(f)
        df = pd.DataFrame(history_data)
        
        # Display the table clearly
        # sort by index descending so newest is at top
        st.dataframe(df.sort_index(ascending=False), use_container_width=True, hide_index=True)
else:
    st.info("System Normal: No anomalies logged.")

# 4. Refresh
time.sleep(1)
st.rerun()