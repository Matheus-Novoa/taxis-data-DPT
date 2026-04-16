import streamlit as st
from pathlib import Path

import data_loader
import charts

CSS_PATH = Path(__file__).parent / "styles.css"

st.set_page_config(
    page_title="Taxis NYC - Dashboard",
    page_icon="🚕",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(f"""
<style>
    {CSS_PATH.read_text()}
</style>
""", unsafe_allow_html=True)

metrics = data_loader.get_metrics()

st.markdown('<div class="header-title">Taxis NYC</div>', unsafe_allow_html=True)
st.markdown('<div class="header-subtitle">Performance Metrics Dashboard</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

cols = st.columns(4)

with cols[0]:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Trips</div>
        <div class="metric-value">{metrics['total_trips']:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Avg Distance</div>
        <div class="metric-value">{metrics['avg_distance']:.2f} km</div>
    </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Avg Fare</div>
        <div class="metric-value">${metrics['avg_fare']:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with cols[3]:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Revenue</div>
        <div class="metric-value">${metrics['total_revenue']/1e6:.2f}M</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

chart_cols = st.columns(2)

with chart_cols[0]:
    st.markdown('<div class="section-title">Key Metrics</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(charts.create_bar_chart(metrics), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with chart_cols[1]:
    st.markdown('<div class="section-title">Distribution</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(charts.create_pie_chart(metrics), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("")
st.markdown("---")
st.markdown(f"""
<div class="footer">
    NYC Taxi Data • 2015-2016 • Powered by Streamlit
</div>
""", unsafe_allow_html=True)