import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


def plot_total_points_distribution(df):
    # Distribution of Total Points
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = sns.histplot(df['total_points'], kde=True, bins=20, color="red")      
    ax.set_title('Distribution of Total Points')
    ax.set_xlabel('Total Points')
    ax.set_ylabel('Frequency')
    fig.set_facecolor('#FFCC00')
    ax.set_facecolor('#FFCC00')
    return fig
