import streamlit as st


def select_pokemon_number(df):
    pokemon_number = st.number_input("Enter Pokemon Number:", 1)
    if not df[df['pokedex_number'] == pokemon_number].empty:
        return pokemon_number
    else:
        st.warning("Pokemon not found!")
        return None
