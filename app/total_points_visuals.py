import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def plot_total_points_distribution(df):
    # Distribution of Total Points
    sns.histplot(df['total_points'], kde=True, bins=20)
    plt.title('Distribution of Total Points')
    plt.xlabel('Total Points')
    plt.ylabel('Frequency')
    plt.show()