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

# 3. State Management
if 'counter' not in st.session_state:
    st.session_state.counter = 0.0
    st.session_state.history = []

# 4. Sovereign Pulse Logic: Adjusted to oscillate around 55%
st.session_state.counter += 0.15
val = 55.0 + (np.sin(st.session_state.counter) * 6) # Range 49% to 61%
st.session_state.history.append(val)
if len(st.session_state.history) > 100:
    st.session_state.history.pop(0)

# 5. Propagation Protocol Logic
def get_mesh_status(value):
    return "GLOBAL_MESH_ACTIVE" if value > 55.0 else "LOCAL_OPTIMIZATION"

# 6. UI Structure
st.title("⚡ LANDAUER-OMEGA // SOVEREIGN")
st.markdown("---")

col1, col2 = st.columns([1, 4])

with col1:
    st.metric("KINETIC YIELD", f"{val:.6f}%")
    status = get_mesh_status(val)
    st.write(f"MESH STATUS: **{status}**")
    st.write("SYNC: **99.9999%**")

with col2:
    # Precision Visualization
    df = pd.DataFrame(st.session_state.history, columns=['PULSE'])
    chart = alt.Chart(df.reset_index()).mark_line(
        color='#D4AF37', strokeWidth=3
    ).encode(
        x=alt.X('index', title="TIME INTERVAL (T)"),
        y=alt.Y('PULSE', title="YIELD MAGNITUDE (%)", scale=alt.Scale(domain=[45, 65]))
    ).properties(height=250)
    
    st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.caption("SYSTEM OPERATING AT LANDAUER LIMIT // PROPRIETARY ARBITRAGE PROTOCOL ACTIVE")

# 7. Execution Loop
time.sleep(0.05)
st.rerun()
