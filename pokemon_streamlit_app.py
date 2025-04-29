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
from app.pokey_heatmap import plot_quad_heatmap

import seaborn as sns
from app.total_points_visuals import plot_total_points_distribution


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

    # Load and clean the data
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

    # versus other pokemon
    display_hp_type_copmparison(df, chosen_pokedata)
    
    # Display the Legendary/Sub Legendary/Mythical/Normal Heatmaps
    st.header("Top Pokémon Comparison Across Generations")
 
    with st.expander("See Top Pokémon Stats Across Generations", expanded=True):
         fig = plot_quad_heatmap(df)
         st.plotly_chart(fig, use_container_width=True)
    
    
    # Apply filters
    filtered_df = apply_filters(df)
    
    
     # Plot Total Points Distribution
    st.subheader("Distribution of Total Points")
    fig = plot_total_points_distribution(df)
    st.pyplot(fig)


if __name__ == "__main__":
    main()



