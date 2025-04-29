import streamlit as st
import plotly.express as px


def display_hp_type_copmparison(df, pokemon_type, hp, chosen_pokedata,):
    # Display a bar chart comparing HP of Pokémon with the same type
    st.subheader("HP Comparison with Other Pokémon of the Same Type:")
    pokemon_type = pokemon_type.values[0]

    # Filter Pokémon with the same type_1
    same_type_pokemon = df[df['type_1'] == pokemon_type].copy()

    # Add a color column to highlight the Pokémon with the given HP
    same_type_pokemon['color'] = same_type_pokemon['pokedex_number'].apply(
        lambda x: 'Highlighted' if x == chosen_pokedata['pokedex_number'].item() else 'Default'
    )

    # Create a bar chart comparing HP
    fig = px.bar(
        same_type_pokemon,
        x='name',  # Assuming the Pokémon names are in a column named 'name'
        y='hp',
        color=same_type_pokemon['color'],
        title=f"HP Comparison for Type: {pokemon_type}",
        labels={'name': 'Pokémon Name', 'hp': 'HP'},
        color_discrete_map={'Highlighted': '#FF0000', 'Default': '#0074BD'}  # Define colours
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)
