import streamlit as st


def select_pokemon_number():
    pokemon_number = st.number_input("Pokemon number", 1)
    if pokemon_number >= 1 and pokemon_number <= 898:
        return pokemon_number

