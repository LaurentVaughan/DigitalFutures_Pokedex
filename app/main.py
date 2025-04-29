import streamlit as st
from app.data_processing import load_and_clean_data
from app.filters import apply_filters
from app.metrics_visuals import (
    display_metrics,
    display_visualizations,
)


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Titanic Dashboard",
        page_icon="🚢",
        layout="wide",
        initial_sidebar_state="auto",
    )
    # Set the title of the app
    st.title("Titanic Dataset Explorer")

    # Load and clean the data
    df = load_and_clean_data("./synthetic_titanic.csv")

    # Apply filters
    filtered_df = apply_filters(df)

    # Display metrics
    display_metrics(filtered_df)

    # Display visualizations
    display_visualizations(filtered_df)


if __name__ == "__main__":
    main()
