import streamlit as st
import plotly.express as px
import pandas as pd

data = "assets/pokemon.csv"
df = pd.read_csv(data)
st.title("Pokemon Dataset Explorer")
st.table(df)
