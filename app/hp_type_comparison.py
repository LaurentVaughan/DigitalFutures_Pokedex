import streamlit as st
import plotly.express as px


def display_hp_type_copmparison(df, chosen_pokedata):
    # Display a dropdown to select the stat for comparison
    stat_options = ['hp', 'attack', 'defense', 'speed', 'abilities_number']
    selected_stat = st.selectbox("Select a stat to compare:", stat_options)

    # Get the type_1 of the selected Pokémon
    pokemon_type = chosen_pokedata['type_1'].values[0]

    # Filter Pokémon with the same type_1
    same_type_pokemon = df[df['type_1'] == pokemon_type].copy()
    
    # Ensure there is only one row for the chosen Pokémon
    chosen_row = chosen_pokedata.iloc[0]

    # Add a color column to highlight the Pokémon with the given stat
    same_type_pokemon['color'] = same_type_pokemon['pokedex_number'].apply(
        lambda x: 'Highlighted' if x == chosen_row['pokedex_number'] else 'Default'
    )

    # Create a bar chart comparing the selected stat
    fig = px.bar(
        same_type_pokemon,
        x='name',  # Assuming the Pokémon names are in a column named 'name'
        y=selected_stat,
        color='color',
        title=f"{selected_stat.capitalize()} Comparison for Type: {pokemon_type}",
        labels={'name': 'Pokémon Name', selected_stat: selected_stat.capitalize()},
        color_discrete_map={'Highlighted': '#FF0000', 'Default': '#0074BD'}  # Define colours
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)

# def display_hp_type_copmparison(df, pokemon_type, hp, chosen_pokedata,):
#     # Display a bar chart comparing HP of Pokémon with the same type
#     st.subheader("HP Comparison with Other Pokémon of the Same Type:")
    
    
#     pokemon_type = chosen_pokedata['type_1'].values[0]

#     # Filter Pokémon with the same type_1
#     same_type_pokemon = df[df['type_1'] == pokemon_type].copy()
    
#     # Ensure there is only one row for the chosen Pokémon
#     chosen_row = chosen_pokedata.iloc[0]

#     # Add a color column to highlight the Pokémon with the given HP
#     same_type_pokemon['color'] = same_type_pokemon['pokedex_number'].apply(
#         lambda x: 'Highlighted' if x == chosen_row['pokedex_number'].item() else 'Default'
#     )

#     # Create a bar chart comparing HP
#     fig = px.bar(
#         same_type_pokemon,
#         x='name',  # Assuming the Pokémon names are in a column named 'name'
#         y='hp',
#         color=same_type_pokemon['color'],
#         title=f"HP Comparison for Type: {pokemon_type}",
#         labels={'name': 'Pokémon Name', 'hp': 'HP'},
#         color_discrete_map={'Highlighted': '#FF0000', 'Default': '#0074BD'}  # Define colours
#     )
#     fig.update_layout(showlegend=False)
#     st.plotly_chart(fig)
    
    
    
