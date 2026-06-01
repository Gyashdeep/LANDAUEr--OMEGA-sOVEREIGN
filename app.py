import streamlit as st
import pandas as pd
import numpy as np
import time
import altair as alt

# 1. Page Configuration
st.set_page_config(page_title="OMEGA-GOLD // SOVEREIGN", layout="wide")

# 2. Styling
st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    [data-testid="stMetricValue"] { color: #D4AF37 !important; font-family: 'Courier New', monospace; font-size: 3rem !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. State
if 'counter' not in st.session_state:
    st.session_state.counter = 0.0
    st.session_state.history = []

# 4. Logic
st.session_state.counter += 0.15
val = 50 + (np.sin(st.session_state.counter) * 10)
st.session_state.history.append(val)
if len(st.session_state.history) > 100:
    st.session_state.history.pop(0)

# 5. UI
st.title("⚡ LANDAUER-OMEGA // SOVEREIGN")
st.markdown("---")

col1, col2 = st.columns([1, 4])
with col1:
    st.metric("KINETIC YIELD", f"{val:.6f}%")
    st.write("STATUS: **ENTROPY INVERSION ACTIVE**")
    st.write("SYNC: **99.9999%**")

with col2:
    # Precision Visualization with Axis Labels
    df = pd.DataFrame(st.session_state.history, columns=['PULSE'])
    chart = alt.Chart(df.reset_index()).mark_line(
        color='#D4AF37', strokeWidth=3
    ).encode(
        x=alt.X('index', title="TIME INTERVAL (T)"),
        y=alt.Y('PULSE', title="YIELD MAGNITUDE (%)", scale=alt.Scale(domain=[30, 70]))
    ).properties(height=250)
    
    st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.caption("SYSTEM OPERATING AT LANDAUER LIMIT // PROPRIETARY ARBITRAGE PROTOCOL")

time.sleep(0.05)
st.rerun()
