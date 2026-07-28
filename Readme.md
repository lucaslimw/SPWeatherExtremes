# Climate Events Probability Aplication - São Paulo State

Interactive dashboard developed with **Python Shiny** for visualization of historical climate event probabilities in the State of São Paulo, Brazil.

The application allows users to explore the probability curves of extreme climate events based on historical records from 1951 to 2025 for different locations and climate variables.

---

## Overview

Climate variability analysis is essential for understanding the occurrence of extreme events and their potential impacts on agriculture, water resources, and environmental systems.

This dashboard provides an interactive interface to visualize probability curves for:

* Precipitation events;
* Maximum temperature events;
* Minimum temperature events.

Users can select different cities and climate variables to analyze the temporal behavior of event probabilities.

---

## Features

* Interactive visualization of climate probability curves;
* Selection of multiple locations in São Paulo State;
* Analysis of different climate variables;
* Interactive Plotly graphics;
* Spatial visualization of study locations;
* Responsive web interface developed with Python Shiny.

---

## Study Area

The application includes climate information from the following locations:

* Campinas
* Cordeirópolis
* Mococa
* Monte Alegre do Sul
* Pindorama
* Ribeirão Preto
* São Paulo

---

## Data

The database contains historical climate information from:

**Period:** 1951–2025

**Variables:**

* Precipitation
* Maximum temperature
* Minimum temperature

The processed datasets are stored locally and loaded dynamically by the application.

---

## Technologies

The project was developed using:

* Python 3.12
* Shiny for Python
* Plotly
* Pandas
* NumPy
* GeoPandas
* Shiny Widgets

Main packages:

```
shiny
shinywidgets
pandas
numpy
plotly
geopandas
pyproj
shapely
```

---

## Project Structure

```
app_livia/
│
├── app.py                  # Main Shiny application
├── config.py               # Configuration files and paths
├── requirements.txt        # Python dependencies
├── .python-version         # Python version specification
│
├── utils/
│   ├── loader.py           # Data loading functions
│   ├── graficos.py         # Plotly visualization functions
│   ├── mapa.py             # Map generation functions
│   ├── legenda.py          # Event labels
│   └── styles.py           # Interface styles
│
├── dados/files
│   └── Climate datasets
│
├── assets/
│   └── style.css           # Custom interface styling
│
└── www/
    └── Images and logos
```

---

The application will be available at:

```
https://lucaslimw.shinyapps.io/app_livia/
```

---

## Data Availability

The climate datasets used in this application are currently stored locally due to ongoing scientific publication processes.

The complete dataset and methodological details will be made available after publication of the associated scientific study.

---

