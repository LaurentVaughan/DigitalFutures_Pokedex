import pandas as pd
import streamlit as st


@st.cache_data
def load_data(filepath):
    """Load the Titanic dataset from a CSV file."""
    return pd.read_csv(filepath)


def clean_numerical_columns(df):
    """Clean numerical columns by filling missing values."""
    df["Age"] = df["Age"].fillna(df["Age"].mean().round())
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
    return df


def clean_categorical_columns(df):
    """Clean categorical columns by filling missing values."""
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df["HasCabin"] = df["Cabin"].notnull().astype(int)
    df.drop(columns=["Cabin"], inplace=True)
    return df


def convert_data_types(df):
    """Convert columns to appropriate data types."""
    df["Sex"] = df["Sex"].astype("category")
    df["Embarked"] = df["Embarked"].astype("category")
    df["Pclass"] = df["Pclass"].astype("category")
    df["Survived"] = df["Survived"].astype("bool")
    df["Age"] = pd.to_numeric(df["Age"].round().astype(int), errors="coerce")
    df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")
    return df


def drop_unnecessary_columns(df):
    """Drop unnecessary columns and duplicates."""
    df.drop(columns=["Ticket"], inplace=True)
    df.drop_duplicates(inplace=True)
    return df


def enrich_dataset(df):
    """Add new features to enrich the dataset."""
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    bins = [-1, 12, 20, 40, 60, 100]
    labels = ["Child", "Teen", "Young Adult", "Adult", "Senior"]
    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)
    return df


def load_and_clean_data(filepath):
    """Load and clean the Titanic dataset."""
    df = load_data(filepath)
    df = clean_numerical_columns(df)
    df = clean_categorical_columns(df)
    df = convert_data_types(df)
    df = drop_unnecessary_columns(df)
    df = enrich_dataset(df)
    return df
