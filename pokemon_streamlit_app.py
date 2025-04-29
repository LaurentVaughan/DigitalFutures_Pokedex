import streamlit as st
import plotly.express as px
import pandas as pd
from selector_function import select_pokemon_number

data = "assets/pokemon.csv"
df = pd.read_csv(data)
st.title("Pokemon Dataset Explorer")
# st.table(df)



pokemon_number = select_pokemon_number()

image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number}.png"

st.image(image_url)