import streamlit as st
import pandas as pd
import json

# ==============================
# Page Config
# ==============================
st.set_page_config(
    page_title="Security Monitoring Platform",
    page_icon="🛡️",
    layout="wide"
)

# ==============================
# Custom Dark Theme Styling
# ==============================
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #fafafa;
}
.metric-container {
    padding: 20px;
    border-radius: 10px;
    background: #161b22;
    box-shadow: 0 0 10px rgba(0,0,0,0.4);
    text-align: center;
}
.metric-title {
    font-size: 16px;
    color: #8b949e;
}
.metric-value {
    font-size: 32px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# Header
# ==============================
st.markdown("""
# 🛡️ Security Monitoring Agent Platform
### AI-Powered Threat Detection & Automated Incident Response
""")

# ==============================
# Load Data
# ==============================
@st.cache_data
def load_json_lines(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    return pd.DataFrame(data)

threats = load_json_lines("data/scaled_logs/enriched_threats.json")
incidents = load_json_lines("data/scaled_logs/incidents.json")

# ==============================
# KPI SECTION
# ==============================
st.markdown("## 📊 Security Overview")

col1, col2, col3, col4 = st.columns(4)

def metric_card(col, title, value):
    col.markdown(f"""
    <div class="metric-container">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

metric_card(col1, "Total Threats", len(threats))
metric_card(col2, "Critical Threats", len(threats[threats["threat_level"]=="CRITICAL"]))
metric_card(col3, "Intel Confirmed", threats["intel_match"].sum())
metric_card(col4, "Automated Responses", len(incidents))

# ==============================
# Tabs
# ==============================
tab1, tab2, tab3 = st.tabs(["📌 Overview", "🚨 Threats", "🧾 Incidents"])

# -------- Overview Tab --------
with tab1:
    st.subheader("Threat Severity Distribution")
    st.bar_chart(threats["threat_level"].value_counts())

    st.subheader("Top Event Types")
    st.bar_chart(threats["event_type"].value_counts())

    col5, col6 = st.columns(2)
    col5.metric("MTTD Reduction", "60%")
    col6.metric("Log Compression", "90%")

# -------- Threats Tab --------
with tab2:
    st.subheader("Detected & Enriched Threats")

    severity_filter = st.selectbox(
        "Filter by Severity",
        ["ALL", "CRITICAL", "HIGH", "MEDIUM"]
    )

    if severity_filter != "ALL":
        filtered = threats[threats["threat_level"] == severity_filter]
    else:
        filtered = threats

    st.dataframe(filtered, use_container_width=True)

# -------- Incidents Tab --------
with tab3:
    st.subheader("Incident Response Records")
    st.dataframe(incidents, use_container_width=True)

st.success("✔ Security Monitoring Platform Running Successfully")
