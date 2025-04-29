import streamlit as st
import pandas as pd
from app.pokemon_visuals import plot_quad_heatmap
import matplotlib.pyplot as plt

data = "assets/pokemon.csv"
df = pd.read_csv(data)

st.title("Pokémon Dataset Explorer")

with st.expander("View Raw Dataset"):
    st.dataframe(df)

# Heatmap
st.subheader("Quad Heatmap: Stat Distribution by Pokémon Status and Generation")
st.markdown("This visual shows **average HP, Attack, Defense, and Speed** for each Pokémon status type (Legendary, Mythical, Sub Legendary, Normal) across generations.")

fig = plot_quad_heatmap(df)
st.plotly_chart(fig)

