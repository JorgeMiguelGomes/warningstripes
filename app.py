# Credits 
# This app is based on the script created by 
# Stven Pestana
# https://github.com/spestana/ulmo-warming-stripes/blob/main/warming-stripes.ipynb
#
# that, in turn, is based on the script developed by 
# Maximilian Nöthe
# https://matplotlib.org/matplotblog/posts/warming-stripes/

# Temperature data for Lisbon from 
# IPMA 
# Source: https://www.ipma.pt/pt/oclima/series.longas/list.jsp
# Period: 1855 to 2018



# import libraries

import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go
import numpy as np
import datetime


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.colors import ListedColormap



#import csv file 

df = pd.read_csv('lisbon_temp_tmintmaxdaily_1855-2018_Lisbon.csv')

df['date'] = pd.to_datetime(df['date'])

df['tmean'] = np.mean([df.tmax, df.tmin], axis=0)


df_annual = df.resample('Y', on='date').mean()
df_annual.year = df_annual.year.astype(int)



print(df_annual.head())

climate_mean = df_annual.tmean.mean()
print(climate_mean)

df_annual['anomaly'] = df_annual.tmean - climate_mean
print(df_annual.head())


cmap = ListedColormap([
    '#08306b', '#08519c', '#2171b5', '#4292c6',
    '#6baed6', '#9ecae1', '#c6dbef', '#deebf7',
    '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a',
    '#ef3b2c', '#cb181d', '#a50f15', '#67000d',
])

# Define the shape of each bar
rect_ll_y = df_annual.anomaly.min() # rectangle lower left y coordinate, minimum anomaly value
rect_height = np.abs(df_annual.anomaly.max()-df_annual.anomaly.min()) # rectangle height, range between min and max anomaly values
year_start = df_annual.year.min() # year to start the plot x axis
year_end = df_annual.year.max() + 1 # year to end the plot x axis

# create a collection with a rectangle for each year
col = PatchCollection([
    Rectangle((x, rect_ll_y), 1, rect_height)
    for x in range(year_start, year_end)
])

# Create the figure, assign the data, colormap and color limits and add it to the figure axes
fig = plt.figure(figsize=(5, 1))

# set up the axes
ax = fig.add_axes([0, 0, 1, 1])
ax.set_axis_off()

# set data, colormap and color limits
col.set_array(df_annual.anomaly) # use the anomaly data for the colormap
col.set_cmap(cmap) # apply our custom red/blue colormap colors
col.set_clim(-rect_height/2, rect_height/2) # set the limits of our colormap
ax.add_collection(col)

# plot anomaly graph
df_annual.plot(x='year', y='anomaly', linestyle='-',lw=1,color='w',ax=ax, legend=False)
# plot horizontal line at zero anomaly
ax.axhline(0, linestyle='dotted', color='w')
# plot a text label
ax.text(df.year.max()+3,-.4,'Lisbon, PT', fontsize=12, fontweight='bold', color='k')

# Make sure the axes limits are correct and save the figure.
ax.set_ylim(-rect_height/2, rect_height/2) # set y axis limits to rectanlge height centered at zero
ax.set_xlim(year_start, year_end); # set x axes limits to start and end year

# save the figure
fig.savefig('warming-stripes-lisbon.jpg', dpi=300, bbox_inches='tight')





