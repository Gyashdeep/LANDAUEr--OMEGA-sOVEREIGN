import streamlit as st
import pandas as pd
import numpy as np
import time
import altair as alt

st.set_page_config(page_title="OMEGA-GOLD // SOVEREIGN", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    [data-testid="stMetricValue"] { color: #FFD700; font-size: 4rem !important; font-family: 'Courier New', monospace; }
    .stApp { background: radial-gradient(circle at center, #1a1a00 0%, #000000 100%); }
    </style>
    """, unsafe_allow_html=True)

if 'counter' not in st.session_state:
    st.session_state.counter = 0.0
    st.session_state.history = []

# Sovereign Pulse Logic: Dampened to Amplitude 10
st.session_state.counter += 0.2
val = 50 + (np.sin(st.session_state.counter) * 10)
st.session_state.history.append(val)

if len(st.session_state.history) > 60:
    st.session_state.history.pop(0)

# Display Metric
st.metric("KINETIC YIELD", f"{val:.4f}%")

# High-Performance Pulse Chart
df = pd.DataFrame(st.session_state.history, columns=['PULSE'])
df['index'] = df.index

chart = alt.Chart(df).mark_line(color='#D4AF37', strokeWidth=4).encode(
    x=alt.X('index', axis=None),
    y=alt.Y('PULSE', scale=alt.Scale(domain=[30, 70]), axis=None)
).properties(width=1000, height=300)

st.altair_chart(chart, use_container_width=True)

st.warning("⚠️ SYSTEM OPERATING AT LANDAUER LIMIT // ENTROPY INVERSION ACTIVE")

time.sleep(0.1)
st.rerun()
