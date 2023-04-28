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

def sales_by_product():
    df = data.groupby('Product type')['Number of products sold'].sum().reset_index()
    print(df)
    fig = px.pie(df, values='Number of products sold', names='Product type',
                    title='Sales by Product Type', hole=0.5,
                    hover_data=['Number of products sold'],
                    color_discrete_sequence=px.colors.qualitative.Set3)
    fig.show()

sales_by_product()