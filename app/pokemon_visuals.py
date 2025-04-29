import plotly.express as px
import pandas as pd
import numpy as np

def plot_quad_heatmap(df):
    focus_columns = ['hp', 'attack', 'defense', 'speed', 'generation', 'status', 'name']
    df_focus = df[focus_columns].dropna()
    df_focus = df_focus[df_focus['status'].isin(['Legendary', 'Mythical', 'Sub Legendary', 'Normal'])]

    status_groups = ['Legendary', 'Mythical', 'Sub Legendary', 'Normal']
    stat_columns = ['hp', 'attack', 'defense', 'speed']
    generations = sorted(df_focus['generation'].unique())

    fig = px.imshow(
        np.zeros((8, 8)),
        text_auto=True
    )

    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    fig = make_subplots(rows=2, cols=2, subplot_titles=status_groups)

    for idx, status in enumerate(status_groups):
        group = df_focus[df_focus['status'] == status]
        name_grid = []

        for stat in stat_columns:
            row = []
            for gen in generations:
                pokes = group[group['generation'] == gen]
                if not pokes.empty:
                    top = pokes.loc[pokes[stat].idxmax()]
                    row.append(top['name'])
                else:
                    row.append("")
            name_grid.append(row)

        name_grid = np.array(name_grid)

        heatmap = go.Heatmap(
            z=np.random.rand(len(stat_columns), len(generations)),
            text=name_grid,
            texttemplate="%{text}",
            colorscale="YlOrRd",
            showscale=False
        )

        row = idx // 2 + 1
        col = idx % 2 + 1
        fig.add_trace(heatmap, row=row, col=col)

    fig.update_layout(
        height=800,
        width=1000,
        title_text="Top Pokémon Names by Stat and Generation (Modern Look)",
        font=dict(size=12),
        plot_bgcolor="white",
    )

    return fig