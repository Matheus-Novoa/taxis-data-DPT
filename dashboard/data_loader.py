import streamlit as st
import pandas as pd


@st.cache_data
def load_metrics_data():
    return pd.read_parquet("data/parquet/metricas.parquet")


def get_metrics():
    df = load_metrics_data()
    return df.iloc[0].to_dict()