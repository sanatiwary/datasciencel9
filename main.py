import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("covid_data.csv")
data = data[["Province_State", "Country_Region", "Last_Update", "Lat", "Long_", "Confirmed", "Recovered", "Deaths", "Active"]]
data.columns = ("State", "Country", "Last Update", "Lat", "Long", "Confirmed", "Recovered", "Deaths", "Active")

data["State"].fillna(value='', inplace=True)

top10Confirmed = pd.DataFrame(data.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values(ascending=False))
fig1 = px.scatter(top10Confirmed, x=top10Confirmed.index, y="Confirmed", size="Confirmed", size_max=120, 
                  color=top10Confirmed.index, title="Top 10 Countries by Confirmed Cases")
# fig1.write_html("Fig1.html", auto_open=True)

top10Deaths = pd.DataFrame(data.groupby("Country")["Deaths"].sum().nlargest(10).sort_values(ascending=False))
fig2 = px.bar(top10Deaths, x="Deaths", y=top10Deaths.index, color_continuous_scale=["deepskyblue", "red"], orientation='h', title="Top 10 Death Cases by Country", height=600)
# fig2.write_html("Fig2.html", auto_open=True)

top10Recovered = pd.DataFrame(data.groupby("Country")["Recovered"].sum().nlargest(10).sort_values(ascending=False))
fig3 = px.bar(top10Recovered, x=top10Recovered.index, y="Recovered", color_continuous_scale=["deepskyblue", "red"], orientation='h', title="Top 10 Recovered Countries")
fig3.write_html("Fig3.html", auto_open=True)

topStatesUS = data["Country"] == "US"
topStatesUS = data[topStatesUS].nlargest(5, "Confirmed")

fig4 = go.Figure(data = [
    go.Bar(name="Confirmed Cases", x=topStatesUS["Confirmed"], y=topStatesUS["Confirmed"], orientation='h'),
    go.Bar(name="Death Cases", x=topStatesUS["Deaths"], y=topStatesUS["State"], orientation='h')
])

fig4.update_layout(title="Most Affected States in USA", height=600)
fig4.write_html("Fig4.html", auto_open=True)