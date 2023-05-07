import pandas as pd
from dash import Dash, dcc, html

# The preprocessed data is saved in a CSV and passed as a param in data which is attributw of Dash interface
data = (
    pd.read_csv("avocado.csv")
    .query("type == 'conventional' and region == 'Albany'")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

app = Dash(__name__)
# This section of code is responsible for converting the attributes to HTML tags. Eg: html.H1 ==> <h1></h1> 
# className is alias to class attribute. Same goes for style

#dcc.Graph is responsible for making the graph. It takes a dictionary as an argument. The dictionary has two keys: data and layout. Data is in the form of CSV and layout we have used for the project is lines
app.layout = html.Div(
    children=[
        html.H1(children="Avocado Analytics",
                className="header-title",
                style={"fontSize": "48px", "color": "red"}),
        html.P(
            children=(
                "Analyze the behavior of avocado prices and the number"
                " of avocados sold in the US between 2015 and 2018"
            ),
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)

# We can attach external CSS files to our Dash app. We can do this by passing a list of dictionaries to the external_stylesheets argument of the Dash constructor. Each dictionary in the list should have a href key with the URL of the CSS file and a rel key with the value stylesheet. We can use this to add Google Fonts to our app. We can also use this to add CSS files from our local machine. For example, if we have a file called style.css in the same directory as our app.py file, we can add it to our app like this:
external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"

if __name__ == "__main__":
    app.run_server(debug=True)