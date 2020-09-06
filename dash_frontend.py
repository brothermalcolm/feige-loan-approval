import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pickle
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Enter 1 if True 0 if False:"),
    html.Div(["Input: ",
              dcc.Input(id='my-input-1', value='Male?', type='text')]),
    html.Div(["Input: ",
              dcc.Input(id='my-input-2', value='Married?', type='text')]),
    html.Div(["Input: ",
              dcc.Input(id='my-input-3', value='Family?', type='text')]),
    html.Div(["Input: ",
              dcc.Input(id='my-input-4', value='Graduate?', type='text')]),
    html.Div(["Input: ",
              dcc.Input(id='my-input-5', value='Employed?', type='text')]),
    html.Div(["Input: ",
              dcc.Input(id='my-input-6', value='Credit-worthy?', type='text')]),
    html.Div(["Input: ",
              dcc.Input(id='my-input-7', value='Urban?', type='text')]),
    html.Div(["Input: ",
              dcc.Input(id='my-input-8', value='Semi-urban?', type='text')]),
    html.Div(["Input: ",
              dcc.Input(id='my-input-9', value='Rural?', type='text')]),
    html.Br(),
    html.Div(id='my-output'),

])

def pred_loan(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    file = '/Users/malcom/Downloads/Feige/models/clf.sav'
    model = pickle.load(open(file, 'rb'))
    new_user = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9]).reshape(1,-1)
    y_pred = model.predict(new_user)
    return y_pred

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
    return 'Output: {}'.format(y[0])


if __name__ == '__main__':
    app.run_server(debug=True)