import pandas as pd
import glob
import numpy as np
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px


def degree2radians(degree):
  # convert degrees to radians
  return degree*np.pi/180
###############----For input----###############
file_list = glob.glob("../FMS_Moonquake/cleaned_data.csv")
df = pd.read_csv(file_list[0])
lon=np.array(df["Long"], dtype=np.float64)
lat=np.array(df["Lat"], dtype=np.float64)
lon=degree2radians(lon)
lat=degree2radians(lat)
radius = 1
df["xs"]=radius*np.cos(lon)*np.cos(lat)
df["ys"]=radius*np.sin(lon)*np.cos(lat)
df["zs"]=radius*np.sin(lat)
print(df)
seis_3D_depth_up = px.scatter_3d(
    df,
    #   x = xs_ev_up,
    #   y = ys_ev_up,
    #   z = zs_ev_up,
    x='xs',
    y='ys',
    z='zs',
    color='Type',
    # mode='markers',
    # name='measured',
    # marker = dict(
    #     size = 3.,
    #     cmax = cmax,
    #     cmin = cmin,
    #     colorbar = dict(
    #         title = 'Source Depth',
    #         titleside = 'right',
    #         titlefont = dict(size = 16,
    #                         color = titlecolor,
    #                         family='Courier New'),
    #         tickmode = 'array',
    #         ticks = 'outside',
    #         ticktext = list(np.arange(cmin,cmax+cbin,cbin)),
    #         tickvals = list(np.arange(cmin,cmax+cbin,cbin)),
    #         tickcolor = titlecolor,
    #         tickfont = dict(size=14, color = titlecolor,
    #                         family='Courier New')
    #     ),
    #     color='Type',
    #     ### choose color option
    #     # color = colours,
    #     ### choose color option
    #     # colorscale = Cscale_EQ,
    #     # showscale = True,
    #     opacity=1.
    # ),
    # hoverinfo='skip'
)

seis_3D_depth_up.show()


titlecolor = 'white'
bgcolor = 'black'


noaxis=dict(showbackground=False,
  showgrid=False,
  showline=False,
  showticklabels=False,
  ticks='',
  title='',
  zeroline=False)
layout = go.Layout(
  autosize=False, width=1200, height=800,
  title = '3D Moonquake Map',
  titlefont = dict(family='Courier New', color=titlecolor),
  showlegend = False,
  scene = dict(
    xaxis = noaxis,
    yaxis = noaxis,
    zaxis = noaxis,
    aspectmode='manual',
    aspectratio=go.layout.scene.Aspectratio(
      x=1, y=1, z=1)),
  paper_bgcolor = bgcolor,
  plot_bgcolor = bgcolor)

plot_data=[seis_3D_depth_up]
fig = go.Figure(data=plot_data, layout=layout)
plot(fig, validate = False, filename='index2.html',
   auto_open=True)