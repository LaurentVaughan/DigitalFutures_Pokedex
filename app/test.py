import streamlit as st
import pandas as pd
from app.pokemon_visuals import plot_quad_heatmap

# Load data
df = pd.read_csv("assets/pokemon.csv")

# Show the heatmap
st.title("📊 Pokémon Stats Heatmap by Status and Generation")
fig = plot_quad_heatmap(df)
st.pyplot(fig)
