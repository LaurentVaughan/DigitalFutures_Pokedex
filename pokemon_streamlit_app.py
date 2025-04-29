import streamlit as st
import plotly.express as px
import pandas as pd

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Podeydex",
        page_icon="🔴",
        layout="wide",
        initial_sidebar_state="auto",
    )

    data = "assets/pokemon.csv"
    df = pd.read_csv(data)
    st.title("Pokemon Dataset Explorer")
    st.table(df[2:5])

if __name__ == "__main__":
    main()
