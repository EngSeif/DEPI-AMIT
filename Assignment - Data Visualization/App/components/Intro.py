import dash_bootstrap_components as dbc
from dash import html

Intro = dbc.Row([
    dbc.Col([
        dbc.Row([
            dbc.Col(
                html.H2("Intro", style={
                    "color": "#2C3E50",
                    "fontWeight": "bold",
                    "fontSize": "2rem",
                    "marginBottom": "10px"
                })
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.P(
                        [
                        "This is a small interactive dashboard built using Dash for analyzing the Titanic dataset from Kaggle. It presents key insights about passenger demographics, survival rates, and class distribution in a visual and intuitive way.",
                        "The project was created by Seif Mohamed as part of the Data Engineering course in the DEPI Initiative."
                        ],
                    style={
                        "color": "#4B6584",
                        "fontSize": "1.1rem",
                        "lineHeight": "1.6"
                    }
                ),
                width = 7
            ),
            dbc.Col(
                html.Img(
                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6WHkMQYjANxb8w14eMqM2dzS357wV2Hn_-Q&s",
                    style={
                        "width": "70%",
                        "borderRadius" : "12px"
                    },
                    className="d-block mx-auto"
                ),
                width = 5
            )
            
        ])
    ])
])
