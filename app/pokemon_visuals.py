# app/pokemon_visuals.py

import plotly.express as px
import pandas as pd

def plot_height_weight_comparison(df, selected_pokemon):
    sample_df = df.sample(10)

    if selected_pokemon.name not in sample_df.index:
        sample_df = pd.concat([sample_df, selected_pokemon.to_frame().T])

    sample_df['is_selected'] = sample_df['#'] == selected_pokemon['#']

    fig = px.scatter(
        sample_df,
        x='height',
        y='weight',
        text='Name',
        color='is_selected',
        color_discrete_map={True: 'red', False: 'blue'},
        title='Height vs Weight Comparison',
        labels={'height': 'Height', 'weight': 'Weight'},
    )

    fig.update_traces(marker=dict(size=12))
    fig.update_layout(showlegend=False)

    return fig
