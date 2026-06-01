import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="OMEGA-GOLD // SOVEREIGN", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    [data-testid="stMetricValue"] { color: #FFD700; font-size: 3rem !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ LANDAUER-OMEGA // GOLD RUSH ⚡")

if 'counter' not in st.session_state:
    st.session_state.counter = 0.0
    st.session_state.history = []

# Generate a high-variance wave
st.session_state.counter += 0.5
val = 50 + (np.sin(st.session_state.counter) * 40) # Massive range: 10 to 90
st.session_state.history.append(val)

if len(st.session_state.history) > 50:
    st.session_state.history.pop(0)

# Display Metric
st.metric("LIVE KINETIC YIELD", f"{val:.4f}%")

# The Fix: Use altair for absolute control over the Y-axis
import altair as alt

df = pd.DataFrame(st.session_state.history, columns=['PULSE'])
df['index'] = df.index

chart = alt.Chart(df).mark_line(color='#D4AF37', strokeWidth=3).encode(
    x='index',
    y=alt.Y('PULSE', scale=alt.Scale(domain=[0, 100]))
).properties(width=800, height=400)

st.subheader("PLANETARY KINETIC ARBITRAGE // MOUNTAIN-VALLEY CURVE")
st.altair_chart(chart, use_container_width=True)

st.warning("⚠️ VOLATILITY OSCILLATOR: ACTIVE")

time.sleep(0.1)
st.rerun()
