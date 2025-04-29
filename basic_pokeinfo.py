import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import 

df = pd.read_csv("assets/pokemon.csv")

def clean_columns():
    df['weight_kg'] = df['weight_kg'].fillna(df['weight_kg'].mean())
    df['catch_rate'] = df['catch_rate'].fillna(df['catch_rate'].mean())
    df['base_friendship'] = df['base_friendship'].fillna(df['base_friendship'].mean())
    df['base_experience'] = df['base_experience'].fillna(df['base_experience'].mean())
    df['type_2'] = df['type_2'].fillna('None')
    df['ability_2'] = df['ability_2'].fillna('None')
    df['ability_hidden'] = df['ability_hidden'].fillna('None')
    df['egg_type_2'] = df['egg_type_2'].fillna('None')
    df['percentage_male'] = df['percentage_male'].fillna('genderless')

clean_columns()

# Ensure 'Number' is treated as int
df['pokedex_number'] = df['pokedex_number'].astype(int)

# Title
st.title("Pokémon Lookup by Number")

# Input
pokemon_number = st.number_input("Enter Pokémon Number", min_value=1)

pokemon_type = df['type_1']

hp = df['hp']

# Search and display
if pokemon_number:
    result = df[df['pokedex_number'] == pokemon_number]

    if not result.empty:
        st.write("Pokémon Data:")
        st.dataframe(result)
         # Get the image URL
        img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number}.png"
        st.image(img_url, caption=f"Pokémon #{pokemon_number}", width=200)
        st.write("Pokémon Type:")
        pokemon_type_1 = result['type_1'].values[0]
        st.write(pokemon_type_1)
        
        # Filter Pokémon with the same type_1
        same_type_pokemon = df[df['type_1'] == pokemon_type_1]
        
        # Create a bar chart comparing HP
        st.write("HP Comparison with Other Pokémon of the Same Type:")
        fig = px.bar(
            same_type_pokemon,
            x='name',  # Assuming the Pokémon names are in a column named 'name'
            y='hp',
            title=f"HP Comparison for Type: {pokemon_type_1}",
            labels={'name': 'Pokémon Name', 'hp': 'HP'},
        )
        st.plotly_chart(fig)
       
    else:
        st.warning("No Pokémon found with that number.")
    
