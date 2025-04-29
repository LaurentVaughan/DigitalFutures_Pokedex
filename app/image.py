import streamlit as st


def display_image(df, pokemon_number):
    # Retrieve the Pokémon name based on the number
    pokemon_name = df[df['pokedex_number'] == pokemon_number]['name'].values[0]

    # Display the Pokémon image with name and number in the caption
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number}.png"
    st.image(image_url, caption=f"{pokemon_name} (#{pokemon_number})", width=200)