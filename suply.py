import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"

data = pd.read_csv("supply_chain_data.csv")

def relationship_between_price_and_revenue():
    fig = px.scatter(data, x='Price', 
                    y='Revenue generated', 
                    color='Product type', 
                    hover_data=['Number of products sold'], 
                    trendline="ols")
    fig.show()

relationship_between_price_and_revenue()