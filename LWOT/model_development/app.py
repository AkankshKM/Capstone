import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from model import Model

# https://www.bootstrapcdn.com/bootswatch/
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
app.layout = dbc.Container([
        dbc.Row(
        dbc.Col(html.H1("LWOT",className='text-center text-primary mb-4'),width=12)),

        dbc.Row([
            dbc.Col([
                dbc.Label("Time of the day"),
                dcc.Input(id='time', value='1', type='text')
                    ]),
            dbc.Col([
                dbc.Label("Day of the week"),
                dcc.Dropdown(id='day',
                            options=[
                                    {'label': 'Monday', 'value': 'Monday'},
                                    {'label': 'Tuesday', 'value': 'Tuesday'},
                                    {'label': 'Wednesday', 'value': 'Wednesday'},
                                    {'label': 'Thursday', 'value': 'Thursday'},
                                    {'label': 'Friday', 'value': 'Friday'},
                                    {'label': 'Saturday', 'value': 'Saturday'},
                                    {'label': 'Sunday', 'value': 'Sunday'}
                                    ],
                                    value='Monday'
                                    )]),
            dbc.Col([
                dbc.Label("Duration of patient stay"),
                dcc.Input(id='duration', value='2', type='text')]),
            dbc.Col([
                dbc.Label("ESI Score"),
                dcc.Dropdown(id='esi',
                                    options=[
                                        {'label': '1', 'value': '1'},
                                        {'label': '2', 'value': '2'},
                                        {'label': '3', 'value': '3'},
                                        {'label': '4', 'value': '4'},
                                        {'label': '5', 'value': '5'}
                                    ],value='1')]),
            dbc.Col([
                dbc.Label("Number of Patients"),
                dcc.Input(id='patientcount', value='3', type='text')]),
   
            ]),
        dbc.Row([
            dbc.Col([
                dbc.Label("Patient got treated or not: 1= patient gets treated, 0= patient Leaves without treatment"),
                html.Div(id='my-output')])
        ]),
        dbc.Row(
                    dbc.Col([
                    dbc.Card(
                        [
                            dbc.CardBody(
                                html.P(
                                    "Confusion Matrix",
                                    className="card-text")
                            ),
                            dbc.CardImg(src="https://raw.githubusercontent.com/AkankshKM/CapstoneImage/main/confusion_matrix.png"),
                        ],
                        style={"width": "24rem"},
                    )
                ], width={'size':5, 'offset':1},
                xs=12, sm=12, md=12, lg=5, xl=5
        )
        ),
        dbc.Row(
            dbc.Col(html.H2("Patient Count",className='text-center text-primary mb-4'),width=12)),
        dbc.Row(
            dbc.Card(
                dbc.CardImg(src="https://raw.githubusercontent.com/AkankshKM/CapstoneImage/main/Prophet.png")
                    )
            )
        
])      
 
@app.callback(
    Output(component_id='my-output', component_property='children'), 
    Input(component_id='time', component_property='value'),
    Input(component_id='day', component_property='value'),
    Input(component_id='duration', component_property='value'),
    Input(component_id='esi', component_property='value'),
    Input(component_id='patientcount', component_property='value')
)
def update_output_div(time,day,duration,esi,patientcount):
    obj = Model()
    result = obj.test_model(time,day,duration,esi,patientcount)
    return 'Output: {}'.format(str(result)) 

if __name__ == '__main__':
    # model = joblib.load("./model.pkl")
    app.run_server(debug=True)