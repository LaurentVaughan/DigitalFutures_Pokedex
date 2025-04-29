import streamlit as st


def add_passenger_class_filter(df):
    """Add a filter for Passenger Class."""
    return st.sidebar.multiselect(
        "Select Passenger Class",
        options=sorted(df["Pclass"].unique()),
        default=sorted(df["Pclass"].unique()),
    )


def add_embarked_port_filter(df):
    """Add a filter for Embarked Port."""
    return st.sidebar.multiselect(
        "Select Embarked Port",
        options=sorted(df["Embarked"].unique()),
        default=sorted(df["Embarked"].unique()),
    )


def filter_dataframe(df, pclass_filter, embarked_filter):
    """Filter the DataFrame based on selected filters."""
    return df[
        (df["Pclass"].isin(pclass_filter))
        & (df["Embarked"].isin(embarked_filter))
    ]


def apply_filters(df):
    """Apply all filters and return the filtered DataFrame."""
    st.sidebar.header("Filters")
    pclass_filter = add_passenger_class_filter(df)
    embarked_filter = add_embarked_port_filter(df)
    return filter_dataframe(df, pclass_filter, embarked_filter)
