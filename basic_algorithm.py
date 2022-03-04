""" Loads the CSV file and filters to components of interest. """

__author__ = "Eve Sherratt, John Jessop"

# Standard library imports
import json

# External imports
import numpy as np
import pandas as pd

# Constants
EARTH_RADIUS = 6.371e6 # Average radius of the Earth in metres

# Code
def load_data(csv_file):
    """ Loads the CSV file and filters to components of interest. """

    df = pd.read_csv(csv_file, usecols=("Material: Name","Company name","Construction times/10","Average cost/cubic metre","Overall EC sum (tonCO2e)"))

    return df


def create_score(df, money_weight, eco_weight, speed_weight):
    """ Basic scoring system. """

    df2 = pd.DataFrame(df["Material: Name"])
    df2.insert(1, "Company name", df["Company name"])

    df2["Money score (%)"] =  (100 - (df["Average cost/cubic metre"]/2)).round().astype(int)

    df2["Eco score (%)"] = (100 - (df["Overall EC sum (tonCO2e)"] * 10000)).round().astype(int)

    df2["Speed score (%)"] = df["Construction times/10"] * 10

    total_weight = int(money_weight) + int(eco_weight) + int(speed_weight)
    df2["Overall score (%)"] = (((df2["Money score (%)"]*int(money_weight)) + (df2["Eco score (%)"]*int(eco_weight)) + (df2["Speed score (%)"]*int(speed_weight))) /  total_weight).round().astype(int)

    return df2
