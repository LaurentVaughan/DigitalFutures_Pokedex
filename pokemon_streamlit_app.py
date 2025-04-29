import streamlit as st
import plotly.express as px
import pandas as pd
from app.filters import apply_filters
from selector_function import select_pokemon_number

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Podeydex",
        page_icon="🔴",
        layout="wide",
        initial_sidebar_state="auto",
    )

    data = "assets/pokemon.csv"
    df = pd.read_csv(data)
    filtered_df = apply_filters(df)
    st.title("Pokemon Dataset Explorer")
    st.table(filtered_df[2:5])
    
    pokemon_number = select_pokemon_number()

    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number}.png"

    st.image(image_url)

if __name__ == "__main__":
    main()
