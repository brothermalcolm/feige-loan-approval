import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from models import pred_loan 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Enter 1 if True 0 if False:"),
    html.Div(["Male?: ",
              dcc.Input(id='my-input-1', value=1, type='text')]),
    html.Div(["Married?: ",
              dcc.Input(id='my-input-2', value=0, type='text')]),
    html.Div(["Family?: ",
              dcc.Input(id='my-input-3', value=0, type='text')]),
    html.Div(["Graduate?: ",
              dcc.Input(id='my-input-4', value=1, type='text')]),
    html.Div(["Employed?: ",
              dcc.Input(id='my-input-5', value=0, type='text')]),
    html.Div(["Credit-worthy?: ",
              dcc.Input(id='my-input-6', value=1, type='text')]),
    html.Div(["Urban?: ",
              dcc.Input(id='my-input-7', value=1, type='text')]),
    html.Div(["Semi-urban?: ",
              dcc.Input(id='my-input-8', value=0, type='text')]),
    html.Div(["Rural?: ",
              dcc.Input(id='my-input-9', value=0, type='text')]),
    html.Br(),
    html.Div(id='my-output'),

])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input-1', component_property='value'),
    Input(component_id='my-input-2', component_property='value'),
    Input(component_id='my-input-3', component_property='value'),
    Input(component_id='my-input-4', component_property='value'),
    Input(component_id='my-input-5', component_property='value'),
    Input(component_id='my-input-6', component_property='value'),
    Input(component_id='my-input-7', component_property='value'),
    Input(component_id='my-input-8', component_property='value'),
    Input(component_id='my-input-9', component_property='value'),
    ]
)
def update_output_div(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    # call function to input features x and output prediction y
    y = pred_loan(x1, x2, x3, x4, x5, x6, x7, x8, x9)
    return 'Output: {}'.format(y)


if __name__ == '__main__':
    app.run_server(debug=True)