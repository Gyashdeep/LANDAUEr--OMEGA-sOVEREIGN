import streamlit as st
import pandas as pd
import numpy as np
import time
import altair as alt

# 1. Page Configuration
st.set_page_config(page_title="OMEGA-GOLD // SOVEREIGN", layout="wide")

# 2. Premium Aesthetic Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    .main { background-color: #000000; font-family: 'JetBrains Mono', monospace; }
    h1 { color: #D4AF37; font-size: 2rem; letter-spacing: -1px; text-transform: uppercase; }
    [data-testid="stMetricValue"] { color: #FFD700; font-size: 4rem !important; font-weight: 700; }
    [data-testid="stMetricLabel"] { color: #888; text-transform: uppercase; letter-spacing: 2px; }
    .status-box { border: 1px solid #D4AF37; padding: 10px; color: #D4AF37; font-size: 0.8rem; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ OMEGA-GOLD // SOVEREIGN NODE")

# 3. Logic Engine
if 'counter' not in st.session_state:
    st.session_state.counter = 0.0
    st.session_state.history = []

st.session_state.counter += 0.15
val = 54.9128 + (np.sin(st.session_state.counter) * 10)
st.session_state.history.append(val)
if len(st.session_state.history) > 60:
    st.session_state.history.pop(0)

# 4. Precision Display
col1, col2 = st.columns([1, 2])
with col1:
    st.metric("KINETIC YIELD", f"{val:.8f}%")
with col2:
    st.markdown("<br><div class='status-box'>STATUS: ENTROPY INVERSION ACTIVE // COMPLIANT</div>", unsafe_allow_html=True)

# 5. Professional Chart (Clean, High-Precision)
df = pd.DataFrame(st.session_state.history, columns=['PULSE'])
df['index'] = df.index

chart = alt.Chart(df).mark_line(color='#D4AF37', strokeWidth=3).encode(
    x=alt.X('index', axis=None),
    y=alt.Y('PULSE', scale=alt.Scale(domain=[40, 70]), axis=None)
).properties(height=250)

st.altair_chart(chart, use_container_width=True)

# 6. Low-Profile footer
st.caption("LATENCY: 0.0001ms | NODE_ID: Ω-SN-1024 | LANDAUER LIMIT: LOCKED")

time.sleep(0.1)
st.rerun()
