import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time

# 1. Page Setup
st.set_page_config(page_title="OMEGA-GOLD // SOVEREIGN", layout="wide")

# 2. Styling: Professional Deep-Black Terminal
st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    [data-testid="stMetricValue"] { color: #D4AF37 !important; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# 3. State: Initialize the pulse history
if 'history' not in st.session_state:
    st.session_state.history = [50.0] * 50

# 4. Logic: Sovereign Sine Pulse
# We calculate a smooth, precise curve for the heartbeat
new_val = 50 + (np.sin(time.time()) * 10)
st.session_state.history.append(new_val)
st.session_state.history.pop(0)

# 5. UI: Precise Metric
st.title("⚡ LANDAUER-OMEGA // SOVEREIGN")
st.metric("KINETIC YIELD", f"{new_val:.6f}%")

# 6. Visualization: The Gold Pulse
df = pd.DataFrame(st.session_state.history, columns=['PULSE'])
chart = alt.Chart(df.reset_index()).mark_line(
    color='#D4AF37', strokeWidth=3
).encode(
    x=alt.X('index', axis=None),
    y=alt.Y('PULSE', scale=alt.Scale(domain=[30, 70]), axis=None)
).properties(height=300)

st.altair_chart(chart, use_container_width=True)

# 7. Update Loop
time.sleep(0.1)
st.rerun()
