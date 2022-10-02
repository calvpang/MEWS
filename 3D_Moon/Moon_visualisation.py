import pandas as pd
import glob
import numpy as np

import rioxarray as rio
import xarray as xa
from rasterio.enums import Resampling

from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px



def get_data(fname = 'lroc_color_poles_4k.tif',
             ds_factor = 2):
    """
    Gets the data from a geotif with filename fname, downscaling int the processs
    Inputs:
        fname (str) : filename of geotif to load
        ds_factor (int) downscale factor
    Output:
        lon, lat, data ([n_lat x n_lon] np arrays)
    """

    xds = rio.open_rasterio(fname)
    xds.attrs['crs'] = 'EPSG:4326'
    new_width = xds.rio.width // ds_factor
    new_height = xds.rio.height // ds_factor

    xds_resampled = xds.rio.set_crs('WGS84').rio.reproject(
        xds.rio.crs,
        shape=(new_height, new_width),
        resampling=Resampling.bilinear,
        SRC_METHOD='NO_GEOTRANSFORM'
    )
    lon = xds_resampled.x.data
    lat = xds_resampled.y.data

    lon = (lon - lon.min()) / (lon.max() - lon.min()) * 360 - 180
    lat = (lat - lat.min()) / (lat.max() - lat.min()) * 180 - 90

    lon, lat = np.meshgrid(lon, lat)

    return lon, lat, xds_resampled.data[0, ...], new_width, new_height

def get_topo(fname='ldem_4.tif',
             new_width=2, new_height=2):
    """
    Gets the data from a geotif with filename fname, downscaling int the processs
    Inputs:
        fname (str) : filename of geotif to load
        ds_factor (int) downscale factor
    Output:
        lon, lat, data ([n_lat x n_lon] np arrays)
    """

    xds = rio.open_rasterio(fname)
    xds.attrs['crs'] = 'EPSG:4326'

    xds_resampled = xds.rio.set_crs('WGS84').rio.reproject(
        xds.rio.crs,
        shape=(new_height, new_width),
        resampling=Resampling.bilinear,
        SRC_METHOD='NO_GEOTRANSFORM'
    )

    return xds_resampled.data[0]

def degree2radians(degree):
    # convert degrees to radians
    return degree*np.pi/180

def mapping_map_to_sphere(lon, lat, radius=1):
    # this function maps the points of coords (lon, lat) to points onto the sphere of radius radius
    lon=np.array(lon, dtype=np.float64)
    lat=np.array(lat, dtype=np.float64)
    lon=degree2radians(lon)
    lat=degree2radians(lat)
    xs=radius*np.cos(lon)*np.cos(lat)
    ys=radius*np.sin(lon)*np.cos(lat)
    zs=radius*np.sin(lat)
    return xs, ys, zs

def mapping_map_to_sphere_df(df, radius=1):
    # this function maps the points of coords (lon, lat) to points onto the sphere of radius radius
    lon=np.array(df["Long"], dtype=np.float64)
    lat=np.array(df["Lat"], dtype=np.float64)
    lon=degree2radians(lon)
    lat=degree2radians(lat)
    df["xs"]=radius*np.cos(lon)*np.cos(lat)
    df["ys"]=radius*np.sin(lon)*np.cos(lat)
    df["zs"]=radius*np.sin(lat)
    return df

# Grab the moon colour map
lon, lat, greys, new_width, new_height = get_data(ds_factor = 5)
xs, ys, zs = mapping_map_to_sphere(lon, lat)
# Grab the topography data
topo = get_topo(new_width=new_width, new_height=new_height)

# # simple 2d version
# cmin = 0
# cmax = 255
# topo_sphere=dict(type='surface',
#     x=xs,
#     y=ys,
#     z=zs,
#     colorscale=Ctopo,
#     surfacecolor=greys,
#     cmin=cmin,
#     cmax=cmax
# )


# Input our moon data
file_list = glob.glob("../cleaned_data.csv")
df = pd.read_csv(file_list[0])
df = mapping_map_to_sphere_df(df)
print(df)

# plot the data in 3d

# colour scale is white to black
Ctopo = [[0, 'rgb(0, 0, 0)'],[1.0, 'rgb(255,255,255)']]
# Set up plot
titlecolor = 'white'
bgcolor = 'black'
noaxis=dict(
    showbackground=False,
    showgrid=False,
    showline=False,
    showticklabels=False,
    ticks='',
    title='',
    zeroline=False
)
layout = go.Layout(
    autosize=False, width=1080, height=720,
    title = 'MEWS',
    titlefont = dict(family='Courier New', color=titlecolor),
    showlegend = True,
    scene = dict(
        xaxis = noaxis,
        yaxis = noaxis,
        zaxis = noaxis,
        aspectmode='manual',
        aspectratio=go.layout.scene.Aspectratio(
        x=1, y=1, z=1)),
    paper_bgcolor = bgcolor,
    plot_bgcolor = bgcolor
)
fig = go.Figure(layout=layout)


# Update it to be 3d with the topo data
cmin = 0
cmax = 255
ratio_topo = 1 + 0.1 * topo / topo.max()
xs_3d = xs*ratio_topo
ys_3d = ys*ratio_topo
zs_3d = zs*ratio_topo
topo_sphere_3d=dict(type='surface',
    x=xs_3d,
    y=ys_3d,
    z=zs_3d,
    colorscale=Ctopo,
    surfacecolor=greys,
    opacity=1.,
    cmin=cmin,
    cmax=cmax,
    showscale=False,
    hoverinfo='skip'
)
fig.add_trace(
    go.Surface(
        x=xs_3d,
        y=ys_3d,
        z=zs_3d,
        colorscale=Ctopo,
        surfacecolor=greys,
        opacity=1.,
        cmin=cmin,
        cmax=cmax,
        showscale=False,
        hoverinfo='skip'
    )
)
cmin = 0.
cmax = 1.
cbin = 1.

# Loop over each data type and add it as a trace
type_colour_pairs = [
    ("Deep Moonquake", "magenta"),
    ("Shallow Moonquake", "blue"),
    ("Meteorite", "red"),
    ("Artifical Impacts", "green"),
]
for moon_type, colour in type_colour_pairs:
    df_type = df[df["Type"] == moon_type]
    fig.add_trace(
        go.Scatter3d(
            mode='markers',
            x=df_type['xs'],
            y=df_type['ys'],
            z=df_type['zs']*1.15,
            name=moon_type,
            marker = dict(
                size = 5.,
                cmax = cmax,
                cmin = cmin,
                opacity=1.,
                color=colour,
            ),
            hoverinfo='skip',
        )
    )

# Edit legend
fig.update_layout(
    legend=dict(
        # x=0,
        # y=1,
        # traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=20,
            color="White"
        ),
        # bgcolor="LightSteelBlue",
        # bordercolor="Black",
        # borderwidth=2
    )
)

# Add logo as title
fig.add_layout_image(
    dict(
        source="MEWS_logo_transparent_background.png",
        # xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom",
        layer="above",
    )
)

plot(
    fig,
    validate=False,
    filename='index.html',
    auto_open=True,
)