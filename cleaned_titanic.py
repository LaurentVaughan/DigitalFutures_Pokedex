import streamlit as st
import pandas as pd

# Set the title of the app
st.title("Titanic Dataset Explorer")
# Load the Titanic dataset
df = pd.read_csv("./synthetic_titanic.csv")

# Clean Data
# Numerical Columns
df["Age"] = df["Age"].fillna(df["Age"].mean().round())
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())

# Categorical Columns
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["HasCabin"] = df["Cabin"].notnull().astype(int)
df.drop(columns=["Cabin"], inplace=True)

# Convert Data Types
df["Sex"] = df["Sex"].astype("category")
df["Embarked"] = df["Embarked"].astype("category")
df["Pclass"] = df["Pclass"].astype("category")
df["Survived"] = df["Survived"].astype("bool")
df["Age"] = pd.to_numeric(df["Age"].round().astype(int), errors="coerce")
df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

# Drop Columns
df.drop(columns=["Ticket"], inplace=True)

# Drop Duplicates
df.drop_duplicates(inplace=True)


# Enrich the dataset

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
bins = [-1, 12, 20, 40, 60, 100]
labels = ["Child", "Teen", "Young Adult", "Adult", "Senior"]
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)

# Show the modified dataset
st.write("DataFrame:")
st.dataframe(df)
st.write("Summary Statistics:")
st.write(df.describe())
st.write("Missing Values:")
st.write(df.isnull().sum())
