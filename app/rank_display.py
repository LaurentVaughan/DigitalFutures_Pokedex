import streamlit as st



def display_height_rank(pokemon_number, df):
    name = df[df['pokedex_number'] == pokemon_number]['name'].iloc[0]
    meters = df[df['pokedex_number'] == pokemon_number]['height_m'].iloc[0]
    df['height_rank'] = df['height_m'].rank(ascending=False, method='min')
    pokemon_row = df[df['pokedex_number'] == pokemon_number]
    height_rank = int(pokemon_row['height_rank'].iloc[0])
    st.text(f"{name} ranks {height_rank} in terms of height with {meters}m!")


def display_weight_rank(pokemon_number, df):
    name = df[df['pokedex_number'] == pokemon_number]['name'].iloc[0]
    kgs = df[df['pokedex_number'] == pokemon_number]['weight_kg'].iloc[0]
    df['weight_rank'] = df['weight_kg'].rank(ascending=False, method='min')
    pokemon_row = df[df['pokedex_number'] == pokemon_number]
    weight_rank = int(pokemon_row['weight_rank'].iloc[0])
    
    st.text(f"{name} ranks {weight_rank} in terms of weight with {kgs}kg!")
   