# Import Necessary Modules 

try:
    import dash
    from dash import dcc, html, Input, Output, Dash
    import plotly.express as px
    import pandas as pd
    import dash_bootstrap_components as dbc
    
except ImportError as e:
    import subprocess
    import sys
    
    print("Some required libraries are missing. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "dash", "plotly", "pandas", "dash-bootstrap-components"])
    
    # Retry imports after installation
    import dash
    from dash import dcc, html, Input, Output, Dash
    import plotly.express as px
    import pandas as pd
    import dash_bootstrap_components as dbc
    
    
app = Dash(__name__, title='Titanic Survival Dashboard', external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    dbc.Row([
        dbc.Col(html.H1("Titanic Dashboard", className="text-center text-primary my-2"), width=12)
    ])
)


if __name__ == "__main__":
    app.run(debug=True)