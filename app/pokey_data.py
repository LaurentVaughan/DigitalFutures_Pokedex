import streamlit as st


def display_pokemon_data(df, pokemon_number):
    """Display Pokémon data in a table."""
    result = df[df['pokedex_number'] == pokemon_number]
    st.subheader("Pokémon Data:")
    st.dataframe(result)
