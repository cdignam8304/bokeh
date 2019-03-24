# -*- coding: utf-8 -*-

#%% Libraries

# Math for trig functions
import math

# Pandas for data management
import pandas as pd

# os methods for manipulating paths
from os.path import dirname, join

# Bokeh basics 
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

# Each tab is drawn by one script
from scripts.titlepage import titlepage_tab
from scripts.ddownexample import ddownexample_tab


#%% Data

# Results data with predictions / actuals etc
#print("Fetching results data...")
#try:
#    df = pd.read_csv(join(dirname(__file__),
#                          "data",
#                          "df_cv_results_sprint3.csv"),
#                    index_col="Unnamed: 0",
#                    keep_default_na=False)
#    print("Got results data! %d rows x %d cols" % (df.shape[0],
#                                                   df.shape[1]))
#except:
#    print("There was a problem getting the results data :(")
#
#
## Get latitude / longitude of countries
#print("Fetching latitude / longitude data...")
#try:
#    df_latlon = pd.read_csv("country_latlon.csv",
#                            sep="\t",
#                           encoding="utf-8")
#    # rename country column
#    df_latlon.columns = ['Country', 'latitude', 'longitude', 'name']
#    # Update Namibia (null in raw data)
#    df_latlon.loc[df_latlon["name"]=="Namibia", ["Country"]] = "NA"
#    print("Got latlon data! %d rows x %d cols" % (df_latlon.shape[0], \
#                                                  df_latlon.shape[1]))
#except:
#    print("There was a problem getting the latlon data :(")
#
#print("Joining results with latlon data...")
#try:
#    # Merge and clean results and latlon data
#    df = pd.merge(df, df_latlon, how="left", on="Country", sort=False)
#    # Add column Location, which is tuple: (latitude, longitude)
#    def geo_tuple(row):
#        return (row["latitude"], row["longitude"])
#    df["Location"] = df.apply(lambda row: geo_tuple(row), axis=1)
#    # Funtion to convert latitude/longitude to x, y coordinates
#    def merc(Coords):
#        # Coordinates = literal_eval(Coords)
#        Coordinates=Coords
#        lat = Coordinates[0]
#        lon = Coordinates[1]
#        
#        r_major = 6378137.000
#        x = r_major * math.radians(lon)
#        scale = x/lon
#        y = 180.0/math.pi * math.log(math.tan(math.pi/4.0 + 
#            lat * (math.pi/180.0)/2.0)) * scale
#        return (x, y)
#    # Apply coordinate conversion
#    df['coords_x'] = df['Location'].apply(lambda x: merc(x)[0])
#    df['coords_y'] = df['Location'].apply(lambda x: merc(x)[1])
#    print("Successfully joined results with latlong data!")
#except:
#    print("There was a problem combining results with latlon data")




#%% Create dashboard

# Create each of the tabs
tab1 = titlepage_tab()
tab2 = ddownexample_tab()
#tab3 = table_tab(flights)
#tab4 = map_tab(map_data, states)
#tab5 = route_tab(flights)

# Put all the tabs into one application
#tabs = Tabs(tabs = [tab1, tab2, tab3, tab4, tab5])
tabs = Tabs(tabs = [tab1, tab2])

# Put the tabs in the current document for display
curdoc().add_root(tabs)