import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="OMEGA-GOLD // SOVEREIGN", layout="wide")

# Extreme Gold Aesthetic
st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    [data-testid="stMetricValue"] { color: #FFD700; font-size: 3rem !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ LANDAUER-OMEGA // GOLD RUSH PULSE ⚡")

# 1. Force state initiation with a wide variance
if 'history' not in st.session_state:
    st.session_state.history = [98.0]

# 2. Extreme Volatility Logic
# Adding 'jitter' so the line never stays flat
jitter = np.random.uniform(-1.0, 1.0)
new_val = st.session_state.history[-1] + jitter
# Bound the pulse between 97 and 99.9 to ensure constant movement
new_val = max(97.0, min(99.9, new_val))
st.session_state.history.append(new_val)

if len(st.session_state.history) > 30:
    st.session_state.history.pop(0)

# 3. Force Render
df = pd.DataFrame(st.session_state.history, columns=['PULSE'])

col1, col2 = st.columns(2)
col1.metric("LIVE KINETIC YIELD", f"{new_val:.4f}%")
col2.metric("STATUS", "CRITICAL // INVERSION")

# Using area_chart to force a filled, visible curve
st.subheader("PLANETARY GOLD RUSH // KINETIC ARBITRAGE")
st.area_chart(df, color="#D4AF37")

st.warning("⚠️ SYSTEM OPERATING AT LANDAUER LIMIT // EXTREME NICHE PULSE ACTIVE")

time.sleep(0.5)
st.rerun()
