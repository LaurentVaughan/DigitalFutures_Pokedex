import streamlit as st
import plotly.express as px


# Metrics Functions
def calculate_total_passengers(filtered_df):
    """Calculate the total number of passengers."""
    return filtered_df["PassengerId"].nunique()


def calculate_overall_survival_rate(filtered_df):
    """Calculate the overall survival rate."""
    return filtered_df["Survived"].mean()


def calculate_average_age(filtered_df):
    """Calculate the average age of passengers."""
    return filtered_df["Age"].mean()


def calculate_survival_rate_by_gender(filtered_df):
    """Calculate the survival rate by gender."""
    return filtered_df.groupby("Sex", observed=False)["Survived"].mean()


def display_metrics(filtered_df):
    """Display key metrics in Streamlit."""
    # Calculate metrics
    total_passengers = calculate_total_passengers(filtered_df)
    overall_survival_rate = calculate_overall_survival_rate(filtered_df)
    average_age = calculate_average_age(filtered_df)
    survival_rate_by_gender = calculate_survival_rate_by_gender(filtered_df)

    # Display metrics in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Passengers", value=total_passengers)
    with col2:
        st.metric(
            label="Overall Survival Rate", value=f"{overall_survival_rate:.2%}"
        )
    with col3:
        st.metric(label="Average Age", value=f"{average_age:.2f}")

    # Add survival rates by gender to separate columns
    gender_cols = st.columns(len(survival_rate_by_gender))
    for col, (gender, rate) in zip(
        gender_cols, survival_rate_by_gender.items()
    ):
        with col:
            st.metric(label=f"Survival Rate ({gender})", value=f"{rate:.2%}")


# Visualization Functions
def create_survival_rate_by_gender_chart(filtered_df):
    """Create a bar chart for survival rate by gender."""
    survival_rate_by_gender = (
        filtered_df.groupby("Sex", observed=False)["Survived"]
        .mean()
        .reset_index()
    )
    survival_rate_by_gender.columns = ["Sex", "Survived"]
    fig = px.bar(
        survival_rate_by_gender,
        x="Sex",
        y="Survived",
        labels={"Sex": "Gender", "Survived": "Survival Rate"},
        title="Survival Rate by Gender",
        text="Survived",
        color="Sex",
    )
    fig.update_traces(texttemplate="%{text:.2%}", textposition="outside")
    return fig


def create_age_distribution_histogram(filtered_df):
    """Create a histogram for age distribution."""
    fig = px.histogram(
        filtered_df,
        x="Age",
        nbins=30,
        title="Age Distribution of Passengers",
        labels={"Age": "Age"},
        color_discrete_sequence=["#636EFA"],
    )
    return fig


def display_visualizations(filtered_df):
    """Display visualizations in Streamlit."""
    # Survival Rate by Gender Bar Chart
    fig1 = create_survival_rate_by_gender_chart(filtered_df)
    st.plotly_chart(fig1)

    # Age Distribution Histogram
    fig2 = create_age_distribution_histogram(filtered_df)
    st.plotly_chart(fig2)
