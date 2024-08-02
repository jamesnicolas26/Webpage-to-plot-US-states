import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Load sample data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

# Create a Plotly figure
fig = px.bar(df, x='State', y='Population')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='US State Populations'),

    html.Div(children='''
        A web application for visualizing state populations.
    '''),

    dcc.Graph(
        id='population-bar-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
