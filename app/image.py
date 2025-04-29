import streamlit as st


def display_image(pokemon_number):
    # Display the Pokémon image based on the selected number
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number}.png"
    st.image(image_url, caption=f"Pokémon #{pokemon_number}", width=200)
