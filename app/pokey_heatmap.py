import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


def plot_quad_heatmap(df):
    focus_columns = ['hp', 'attack', 'defense', 'speed', 'generation', 'status', 'name']
    df_focus = df[focus_columns].dropna()
    df_focus = df_focus[df_focus['status'].isin(['Legendary', 'Mythical', 'Sub Legendary', 'Normal'])]

    status_groups = ['Legendary', 'Sub Legendary', 'Mythical', 'Normal']
    stat_columns = ['hp', 'attack', 'defense', 'speed']
    generations = sorted(df_focus['generation'].unique())
    generation_labels = [f"Gen {g}" for g in generations]

    fig = make_subplots(
        rows=4,
        cols=1,
        shared_xaxes=False,
        subplot_titles=status_groups,
        vertical_spacing=0.08,
        specs=[[{"type": "heatmap"}],
               [{"type": "heatmap"}],
               [{"type": "heatmap"}],
               [{"type": "heatmap"}]]
    )

    for idx, status in enumerate(status_groups):
        group = df_focus[df_focus['status'] == status]
        name_grid = []
        stat_grid = []

        for stat in stat_columns:
            name_row = []
            value_row = []
            for gen in generations:
                pokes = group[group['generation'] == gen]
                if not pokes.empty:
                    top = pokes.loc[pokes[stat].idxmax()]
                    name_row.append(top['name'].replace(" ", "<br>"))
                    value_row.append(top[stat])
                else:
                    name_row.append("")
                    value_row.append(0)
            name_grid.append(name_row)
            stat_grid.append(value_row)

        name_grid = np.array(name_grid)
        stat_grid = np.array(stat_grid)

        stat_min = np.min(stat_grid)
        stat_max = np.max(stat_grid)
        if stat_max - stat_min != 0:
            stat_grid_normalized = (stat_grid - stat_min) / (stat_max - stat_min)
        else:
            stat_grid_normalized = stat_grid

        heatmap = go.Heatmap(
            z=stat_grid_normalized,
            text=name_grid,
            texttemplate="%{text}",
            colorscale="YlOrRd",
            showscale=False,
            x=generation_labels,
            y=stat_columns,
            textfont={"size": 14},
            hovertemplate="Stat: %{y}<br>Generation: %{x}<br>Pokémon: %{text}<br>Value: %{z:.2f}<extra></extra>",
            xgap=0,
            ygap=0
        )

        row = idx + 1
        col = 1
        fig.add_trace(heatmap, row=row, col=col)

    fig.update_layout(
        height=1600,
        width=1000,
        title_text="Top Pokémon by Stat and Generation (Normalized)",
        font=dict(size=14),
        margin=dict(t=180, l=0, r=0, b=0),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        uniformtext=dict(minsize=12, mode='hide')
    )

    return fig
