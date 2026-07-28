import pandas as pd
import plotly.express as px


# Coordenadas aproximadas dos municípios
CIDADES = pd.DataFrame({
    "cidade": [
        "Campinas",
        "Cordeirópolis",
        "Mococa",
        "Monte Alegre do Sul",
        "Pindorama",
        "Ribeirão Preto",
        "São Paulo"
    ],

    "lat": [
        -22.905,
        -22.481,
        -21.467,
        -22.681,
        -21.185,
        -21.177,
        -23.550
    ],

    "lon": [
        -47.060,
        -47.451,
        -47.005,
        -46.681,
        -48.907,
        -47.810,
        -46.633
    ]
})


def criar_mapa():

    fig = px.scatter_map(
        CIDADES,

        lat="lat",
        lon="lon",

        hover_name="cidade",

        zoom=6,

        center={
            "lat": -22.5,
            "lon": -47.3
        },

        height=500,
    )

    fig.update_traces(
        marker=dict(
            size=12
        )
    )

    fig.update_layout(
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        )
    )

    return fig