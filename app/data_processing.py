import pandas as pd
import streamlit as st

@st.cache_data
def load_data(filepath):
    """Load the Pokémon dataset from a CSV file."""
    return pd.read_csv(filepath)


def clean_numerical_columns(df):
    """Fill missing values in numerical columns with the mean."""
    df["weight_kg"] = df["weight_kg"].fillna(df["weight_kg"].mean())
    df["catch_rate"] = df["catch_rate"].fillna(df["catch_rate"].mean())
    df["base_friendship"] = df["base_friendship"].fillna(df["base_friendship"].mean())
    df["base_experience"] = df["base_experience"].fillna(df["base_experience"].mean())
    df["egg_cycles"] = df["egg_cycles"].fillna(df["egg_cycles"].mean())
    return df


def clean_categorical_columns(df):
    """Fill missing values in categorical columns with placeholders."""
    df["type_2"] = df["type_2"].fillna("None")
    df["ability_1"] = df["ability_1"].fillna("Unknown")
    df["ability_2"] = df["ability_2"].fillna("None")
    df["ability_hidden"] = df["ability_hidden"].fillna("None")
    df["growth_rate"] = df["growth_rate"].fillna("Unknown")
    df["egg_type_1"] = df["egg_type_1"].fillna("Unknown")
    df["egg_type_2"] = df["egg_type_2"].fillna("None")
    return df


def handle_gender_column(df):
    """Handle missing values in the gender column."""
    df["is_genderless"] = df["percentage_male"].isna().astype(int)
    df["percentage_male"] = df["percentage_male"].fillna(-1)
    return df


def convert_data_types(df):
    """Convert columns to appropriate data types."""
    df["type_1"] = df["type_1"].astype("category")
    df["type_2"] = df["type_2"].astype("category")
    df["ability_1"] = df["ability_1"].astype("category")
    df["ability_2"] = df["ability_2"].astype("category")
    df["ability_hidden"] = df["ability_hidden"].astype("category")
    df["growth_rate"] = df["growth_rate"].astype("category")
    df["egg_type_1"] = df["egg_type_1"].astype("category")
    df["egg_type_2"] = df["egg_type_2"].astype("category")
    return df


def drop_duplicates(df):
    """Drop duplicate rows if any."""
    df.drop_duplicates(inplace=True)
    return df


def load_and_clean_data(filepath):
    """Load and fully clean the Pokémon dataset."""
    df = load_data(filepath)
    df = clean_numerical_columns(df)
    df = clean_categorical_columns(df)
    df = handle_gender_column(df)
    df = convert_data_types(df)
    df = drop_duplicates(df)
    df['pokedex_number'] = df['pokedex_number'].astype(int)
    return df
