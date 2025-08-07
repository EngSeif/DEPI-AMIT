import dash_bootstrap_components as dbc
from dash import html

HeadTitle =  dbc.Row(
    [
        dbc.Col(
            html.H1("Titanic Dashboard", className="text-center my-2",
                    style={
                        "color":"#2C3E50"
                        }
                    ), 
            width=12
            )
     ]
    )