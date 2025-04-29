import streamlit as st
import plotly.express as px
import pandas as pd
from app.filters import apply_filters
from app.data_processing import load_and_clean_data
from app.selector_function import select_pokemon_number
from app.image import display_image
from app.pokey_data import display_pokemon_data
from app.hp_type_comparison import display_hp_type_copmparison
from app.rank_display import display_height_rank, display_weight_rank


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Podeydex",
        page_icon="🔴",
        layout="wide",
        initial_sidebar_state="auto",
    )

    st.title("Pokemon Dataset Explorer")

    data = "assets/pokemon.csv"

    # Loaad and clean the data
    df = load_and_clean_data(data)

    # Input for Pokémon number
    pokemon_number = select_pokemon_number(df)
    chosen_pokedata = df[df['pokedex_number'] == pokemon_number]

    if pokemon_number is None:
        st.warning("Please select a Pokémon number.")
        return

    # display image
    display_image(df, pokemon_number)
 
    # Display height and weight ranks
    display_height_rank(pokemon_number, df)
    display_weight_rank(pokemon_number, df)

    # display dataframe
    display_pokemon_data(df, pokemon_number)

    # pokemon data variables
    pokemon_type = df['type_1']
    hp = df['hp']

    # versus other pokemon
    display_hp_type_copmparison(df, chosen_pokedata)


if __name__ == "__main__":
    main()
