import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/bijoordzen/temperatureplot/main/temp.csv')
p =(df['temp'])
q = (df['date and time'])
a = p[:50]
b = q[:50]
app = dash.Dash()

app.layout = html.Div([html.H1("Team B"),
			 html.Div("Sensor Plots"),
             html.Label('Choose Data to Display'),
             dcc.Dropdown(
                 id = 'first-dropdown',
                 options =[
                     {'label':'SD Card Temeprature Sensor Data ','value': 'sdcard'},
                     {'label':'Realtime Temeprature Sensor Data ','value': 'lm35rlt'},
                     {'label':'Coolant  Temperature','value': 'coolant'},
                     {'label':'Fuel Temperature','value': 'fuel'}
                     ],
                 multi = True
                         ),
			 dcc.Graph(
                id='graph',
                figure={
                    'data': [
                {'x': b, 'y': a, 'type': 'line'},
                ],
            'layout': {
                'title': 'Temperature vs Time'
                      }
                      }
                      )
                 
])

if __name__ == '__main__':
	app.run_server()