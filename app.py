import streamlit as st
import pandas as pd
import numpy as np
import time
import altair as alt

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="SOVEREIGN // OMEGA-GOLD", layout="wide")

# --- PROFESSIONAL AESTHETICS (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { color: #D4AF37; }
    [data-testid="stMetricValue"] { color: #FFD700 !important; font-family: 'JetBrains Mono', monospace; font-size: 3rem !important; }
    .metric-label { font-family: 'Inter', sans-serif; text-transform: uppercase; letter-spacing: 2px; color: #666; }
    </style>
    """, unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'counter' not in st.session_state:
    st.session_state.counter = 0.0
    st.session_state.history = []

# --- SOVEREIGN PULSE LOGIC ---
st.session_state.counter += 0.15
val = 50 + (np.sin(st.session_state.counter) * 10)
st.session_state.history.append(val)
if len(st.session_state.history) > 60:
    st.session_state.history.pop(0)

# --- UI STRUCTURE ---
col1, col2 = st.columns([1, 4])

with col1:
    st.markdown("### Ω-SOVEREIGN")
    st.markdown("<div class='metric-label'>Kinetic Yield</div>", unsafe_allow_html=True)
    st.metric("", f"{val:.6f}%")
    st.markdown("---")
    st.write("**STATUS:** ENTROPY_INVERSION")
    st.write("**FREQ:** 440.02Hz")
    st.write("**LIMIT:** LANDAUER_ACTIVE")

with col2:
    # Precision Visualization
    df = pd.DataFrame(st.session_state.history, columns=['PULSE'])
    chart = alt.Chart(df.reset_index()).mark_line(
        color='#D4AF37', strokeWidth=3
    ).encode(
        x=alt.X('index', axis=None),
        y=alt.Y('PULSE', scale=alt.Scale(domain=[35, 65]), axis=None)
    ).properties(height=250)
    
    st.altair_chart(chart, use_container_width=True)

# --- SYSTEM FOOTER ---
st.caption("CORE_INIT: 0x999900 // SYSTEM OPERATING WITHIN NOMINAL PARAMETERS")

time.sleep(0.05)
st.rerun()
