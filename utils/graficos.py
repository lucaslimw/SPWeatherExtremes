import plotly.graph_objects as go

from utils.legenda import LEGENDAS


def criar_grafico(df, cidade, variavel, modo, evento):

    fig = go.Figure()

    legenda = LEGENDAS.get(variavel, {})

    if not legenda:
        return fig
    
    for coluna in df.columns:

        if coluna == "ano":
            continue

        if modo == "uma" and coluna != evento:
            continue

        fig.add_trace(
            go.Scatter(
                x=df["ano"],
                y=df[coluna],
                mode="lines",
                name=legenda[coluna],
                line=dict(width=2),
            )
        )

    fig.update_layout(

        title={
            "text": cidade,
            "x": 0.5,
        },

        template="simple_white",

        hovermode="x unified",

        xaxis=dict(
            title="Year",
            showgrid=True,
        ),

        yaxis=dict(
            title="Probability",
            range=[0, 1],
            tickformat=".1f",
        ),

        legend_title="Event",

        height=650,
    )

    return fig