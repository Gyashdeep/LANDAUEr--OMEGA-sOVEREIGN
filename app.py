import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="OMEGA-GOLD // SOVEREIGN", layout="wide")

# Extreme CSS for the Gold Aesthetic
st.markdown("""
    <style>
    .main { background-color: #000000; }
    h1 { color: #D4AF37; font-family: 'Courier New', monospace; }
    [data-testid="stMetricValue"] { color: #FFD700; font-size: 3rem !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ LANDAUER-OMEGA // GOLD PULSE ⚡")

# 1. Initialize State with a time-counter for the Sine Wave
if 'counter' not in st.session_state:
    st.session_state.counter = 0
    st.session_state.history = []

# 2. Forced Sine Wave Logic (Guaranteed to create Curves)
# The sine function creates natural peaks and valleys
val = 98.0 + (np.sin(st.session_state.counter) * 1.5)
st.session_state.counter += 0.2 # Speed of the pulse

st.session_state.history.append(val)
if len(st.session_state.history) > 50:
    st.session_state.history.pop(0)

# 3. Render Dashboard
col1, col2 = st.columns(2)
col1.metric("LIVE KINETIC YIELD", f"{val:.4f}%")
col2.metric("ENTROPY STATUS", "OSCILLATING")

# Use a DataFrame to force the chart to acknowledge the sequence
df = pd.DataFrame(st.session_state.history, columns=['GOLD_RUSH_PULSE'])

st.subheader("PLANETARY KINETIC ARBITRAGE // MOUNTAIN-VALLEY CURVE")
st.area_chart(df, color="#D4AF37")

st.warning("⚠️ EXTREME NICHE // WAVEFORM ACTIVE")

time.sleep(0.1)
st.rerun()
