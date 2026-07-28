from shiny import reactive
from shiny.express import input, ui
from shinywidgets import render_plotly
import plotly.graph_objects as go


from utils.loader import (
    carregar_dados,
    listar_cidades,
    listar_variaveis,
)
from utils.legenda import LEGENDAS
from utils.graficos import criar_grafico
from utils.mapa import criar_mapa
ui.include_css("assets/style.css")

# --------------------------------------------------
# Carrega todos os dados
# --------------------------------------------------

dados = carregar_dados()

cidades = listar_cidades(dados)
variaveis = listar_variaveis(dados)

# --------------------------------------------------
# Interface
# --------------------------------------------------

ui.page_opts(
    title=" ",
    fillable=True,
)

with ui.div(class_="header"):

    ui.img(
        src="Logo_iac.JPG",
        style="height: 70px; width:auto;"
    )

    with ui.div(class_="titulo"):

        ui.h1("Probability of Climate Events in São Paulo State")

        ui.p("Historical Data (1951–2025)")

    ui.img(
        src="logotipo_pos_graduacao.jpg",
        style="height: 70px; width:auto;"
    )

# --------------------------------------------------
# Obtém dataframe selecionado
# --------------------------------------------------

@reactive.effect
def atualizar_eventos():

    variavel = input.variavel()
    if variavel is None:
        return
    legenda = LEGENDAS.get(variavel, {})
    if not legenda:
        return
    
    ui.update_select(
        "evento",
        choices=legenda,
        selected=list(legenda.keys())[0],
    )

@reactive.calc
def df_atual():

    chave = (
        input.cidade(),
        input.variavel(),
    )

    return dados[chave]["dados"]
# --------------------------------------------------
# Gráfico
# --------------------------------------------------

with ui.navset_tab():

    with ui.nav_panel("Probabilities"):

        with ui.layout_sidebar():

            with ui.sidebar():
            

                ui.h3("Filters")

                ui.input_select(
                "cidade",
                "City",
                choices=cidades,
                selected=cidades[0] if cidades else None,
                )

                ui.input_select(
                "variavel",
                "Variable",
                choices=variaveis,
                selected=variaveis[0] if variaveis else None,
                )

                ui.input_radio_buttons(
                    "modo",
                    "Curves",
                    choices={
                    "todas": "All",
                        "uma": "Single curve",
                    },
                )

                ui.input_select(
                    "evento",
                    "Event",
                    choices=[],
                )

            with ui.card(full_screen=True):

                ui.card_header("Probability Curves")

                @render_plotly
                def grafico():
                    df = df_atual()

                    return criar_grafico(
                        df=df,
                        cidade=input.cidade(),
                        variavel=input.variavel(),
                        modo=input.modo(),
                        evento=input.evento(),
                        )


    with ui.nav_panel("City Map"):

        with ui.card():

            ui.card_header("Location of study cities")

            @render_plotly
            def mapa():
                return criar_mapa()


