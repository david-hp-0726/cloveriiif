import cloveriiif
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    cloveriiif.Cloveriiif(
        iiifLink=None
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)
